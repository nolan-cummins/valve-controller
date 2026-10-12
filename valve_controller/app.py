import json
import sys
from pathlib import Path

from PySide6.QtCore import QCoreApplication, QIODevice, Qt
from PySide6.QtGui import QAction, QActionGroup, QCloseEvent, QIcon, QKeySequence
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from PySide6.QtWidgets import QApplication, QComboBox, QFileDialog, QMainWindow

from .ui_main import Ui_MainWindow

HERE = Path(__file__).parent


def tr(text: str) -> str:
    return QCoreApplication.translate("MainWindow", text, None)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        icon = QIcon(str(HERE / "logo.png"))
        self.setWindowIcon(icon)
        QApplication.setWindowIcon(icon)
        self.setWindowTitle("Valve Control")

        self.serial = QSerialPort(self)
        self.serial.readyRead.connect(self.read_serial_data)
        self.serial.errorOccurred.connect(self.on_serial_error)
        self.buffer, self.com_port, self.response, self.command_string = b'', '', '', ''

        # Serial menu: static "Refresh Devices" entry, then one checkable action per port
        self.port_group = QActionGroup(self)
        self.port_group.setExclusive(False)
        self.refresh_action = QAction("Refresh Devices", self)
        self.refresh_action.setShortcut(QKeySequence("F5"))
        self.refresh_action.triggered.connect(self.findPorts)
        self.menuSerial.addAction(self.refresh_action)
        self.menuSerial.addSeparator()
        self.menuSerial.aboutToShow.connect(self.findPorts)
        self.findPorts()

        combobox = self.position_combobox
        combobox.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)
        combobox.lineEdit().editingFinished.connect(self.update_line_item)

        self.close_all_button.setStyleSheet("background-color: red; color: white;")
        buttons = [
            (self.set_button, self.set_item),
            (self.load_button, self.load_item),
            (self.add_item_button, lambda: combobox.addItem(f"Position {combobox.count()+1}")),
            (self.delete_item_button, self.delete_item),
            (self.close_all_button, self.close_all_valves),
        ]
        for button, handler in buttons:
            button.clicked.connect(handler)

        for action, handler in [
            (self.actionLoad_Positions, self.load_positions),
            (self.actionSave_Positions, self.save_positions),
        ]:
            action.triggered.connect(handler)

        self.valve_buttons = [self.valve_1_button, self.valve_2_button, self.valve_3_button, self.valve_4_button]
        self.valve_dict = {valve.objectName(): valve for valve in self.valve_buttons}
        for button in self.valve_buttons:
            button.clicked.connect(self.on_valve)
            button.setFocusPolicy(Qt.NoFocus)

    def update_line_item(self) -> None:  # in-place editing of combobox items
        combobox = self.position_combobox
        if combobox.currentIndex() >= 0:
            combobox.setItemText(combobox.currentIndex(), combobox.currentText())

    def port_actions(self) -> list[QAction]:
        return self.port_group.actions()

    def findPorts(self) -> None:  # rebuild port list; keeps the open port checked if still present
        ports = QSerialPortInfo.availablePorts()
        present = {p.portName() for p in ports}
        for action in self.port_actions():
            if action.objectName() not in present:
                if action.isChecked():
                    self.disconnect_serial("device removed")
                self.port_group.removeAction(action)
                self.menuSerial.removeAction(action)
                action.deleteLater()
        known = {a.objectName() for a in self.port_actions()}
        for p in sorted(ports, key=lambda p: p.portName()):
            if p.portName() in known:
                continue
            label = f"{p.portName()} - {p.description()}" if p.description() else p.portName()
            action = QAction(label, self, checkable=True)
            action.setObjectName(p.portName())
            action.triggered.connect(self.on_serial)
            self.port_group.addAction(action)
            self.menuSerial.addAction(action)
        if not ports and not self.port_actions():
            self.serial_stream.setText(tr("Serial Stream: No devices found | N/A"))

    def disconnect_serial(self, reason: str = "") -> None:
        if self.serial.isOpen():
            self.serial.close()
        for action in self.port_actions():
            action.setChecked(False)
        suffix = f" ({reason})" if reason else ""
        self.serial_stream.setText(tr(f"Serial Stream: Disconnected{suffix} | N/A"))

    def on_serial(self) -> None:  # connect to the clicked port, or disconnect if it was already open
        action = self.sender()
        if self.serial.isOpen():
            self.serial.close()
        for other in self.port_actions():
            if other is not action:
                other.setChecked(False)
        if not action.isChecked():
            self.disconnect_serial()
            return
        self.com_port = action.objectName()
        self.serial.setPortName(self.com_port)
        self.serial.setBaudRate(QSerialPort.Baud115200)
        self.serial.setDataBits(QSerialPort.Data8)
        self.serial.setParity(QSerialPort.NoParity)
        self.serial.setStopBits(QSerialPort.OneStop)
        self.serial.setFlowControl(QSerialPort.NoFlowControl)
        if self.serial.open(QIODevice.ReadWrite):
            self.serial_stream.setText(tr(f"Serial Stream: Connected to {action.text()} | No Response Yet"))
        else:
            err = self.serial.errorString()
            action.setChecked(False)
            self.serial_stream.setText(tr(f"Serial Stream: {err} | N/A"))

    def on_serial_error(self, error) -> None:  # e.g. cable pulled mid-session
        if error == QSerialPort.SerialPortError.ResourceError:
            self.disconnect_serial("device lost")
            self.findPorts()

    def read_serial_data(self) -> None:
        try:
            data = self.serial.readAll().data()
            if not data:
                return
            self.buffer += data
            while b'\n' in self.buffer:
                line, self.buffer = self.buffer.split(b'\n', 1)
                self.response = line.decode('utf_8', errors='replace')
                cmd = self.command_string.replace("\n", "")
                self.serial_stream.setText(tr(f"Serial Stream: {cmd} | {self.response.replace(chr(10), '')}"))
        except Exception as e:
            print(f"Error reading serial data: {e}")

    def load_positions(self) -> None:  # load valve positions from .json file
        file_path, _ = QFileDialog.getOpenFileName(self, "Load Positions", "", ".json Files (*.json*)")
        if not file_path:
            return
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                valve_positions = json.load(f)
        except (OSError, json.JSONDecodeError) as e:
            self.serial_stream.setText(tr(f"Load failed: {e}"))
            return
        self.position_combobox.clear()
        for position, data in valve_positions.items():
            self.position_combobox.addItem(position, data)

    def save_positions(self) -> None:  # save valve positions to .json file
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Positions", "", ".json Files (*.json)")
        if not file_path:
            return
        combobox = self.position_combobox
        positions = {combobox.itemText(i): combobox.itemData(i) for i in range(combobox.count())}
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(positions, f, indent=4)
        except OSError as e:
            self.serial_stream.setText(tr(f"Save failed: {e}"))

    def set_item(self) -> None:  # store current button states in the selected position
        states = {v.objectName(): v.isChecked() for v in self.valve_buttons}
        self.position_combobox.setItemData(self.position_combobox.currentIndex(), states, Qt.ItemDataRole.UserRole)

    def load_item(self) -> None:  # apply selected position to the buttons
        for button, state in (self.position_combobox.currentData() or {}).items():
            self.on_valve(button, state)

    def delete_item(self) -> None:
        self.position_combobox.removeItem(self.position_combobox.currentIndex())

    def on_valve(self, button: str = '', state: bool = False) -> None:
        sender_obj = self.sender()
        if sender_obj.objectName() in ("load_button", "close_all_button"):
            button_obj = self.valve_dict.get(button)
            if button_obj is None:
                print(f"Invalid valve name: {button}")
                return
            button_obj.setChecked(state)
            status = 'ON' if state else 'OFF'
        else:
            button = sender_obj.objectName()
            status = 'ON' if sender_obj.isChecked() else 'OFF'
        if button in self.valve_dict:
            n = button.split('_')[1]
            self.send_serial(cmd=f"{n};{status}", category="V")
            getattr(self, f"valve_{n}_status").setText(tr(f"Status: {status}"))

    def close_all_valves(self) -> None:
        for button in self.valve_buttons:
            self.on_valve(button.objectName(), False)

    def send_serial(self, cmd: str, category: str) -> None:  # no-op on the wire if no port is open
        self.command_string = f'{category};{cmd}\n' if category else cmd
        self.response = "No response yet"
        if self.serial.isOpen():
            self.serial.write(self.command_string.encode('utf_8'))
        self.serial_stream.setText(tr(f"Serial Stream: '{self.command_string.strip()}' | '{self.response}'"))

    def closeEvent(self, event: QCloseEvent) -> None:
        if self.serial.isOpen():
            self.serial.close()
        super().closeEvent(event)


def main() -> None:
    if sys.platform == "win32":  # taskbar icon grouping
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('int.fmp.valves')
    app = QApplication.instance() or QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
