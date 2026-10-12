# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainhhVOJw.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(725, 260)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.actionLoad_Positions = QAction(MainWindow)
        self.actionLoad_Positions.setObjectName(u"actionLoad_Positions")
        self.actionSave_Positions = QAction(MainWindow)
        self.actionSave_Positions.setObjectName(u"actionSave_Positions")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_6 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.position_combobox = QComboBox(self.centralwidget)
        self.position_combobox.addItem("")
        self.position_combobox.setObjectName(u"position_combobox")
        self.position_combobox.setMinimumSize(QSize(300, 0))
        self.position_combobox.setEditable(True)

        self.horizontalLayout_2.addWidget(self.position_combobox)

        self.load_button = QPushButton(self.centralwidget)
        self.load_button.setObjectName(u"load_button")
        self.load_button.setMaximumSize(QSize(74, 16777215))

        self.horizontalLayout_2.addWidget(self.load_button)

        self.set_button = QPushButton(self.centralwidget)
        self.set_button.setObjectName(u"set_button")
        self.set_button.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_2.addWidget(self.set_button)

        self.add_item_button = QPushButton(self.centralwidget)
        self.add_item_button.setObjectName(u"add_item_button")
        self.add_item_button.setMaximumSize(QSize(74, 16777215))

        self.horizontalLayout_2.addWidget(self.add_item_button)

        self.delete_item_button = QPushButton(self.centralwidget)
        self.delete_item_button.setObjectName(u"delete_item_button")
        self.delete_item_button.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_2.addWidget(self.delete_item_button)

        self.close_all_button = QPushButton(self.centralwidget)
        self.close_all_button.setObjectName(u"close_all_button")
        self.close_all_button.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_2.addWidget(self.close_all_button)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.valve_1_button = QPushButton(self.centralwidget)
        self.valve_1_button.setObjectName(u"valve_1_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.valve_1_button.sizePolicy().hasHeightForWidth())
        self.valve_1_button.setSizePolicy(sizePolicy1)
        self.valve_1_button.setMinimumSize(QSize(100, 100))
        font = QFont()
        font.setPointSize(12)
        self.valve_1_button.setFont(font)
        self.valve_1_button.setCheckable(True)

        self.verticalLayout_4.addWidget(self.valve_1_button)

        self.valve_1_status = QLabel(self.centralwidget)
        self.valve_1_status.setObjectName(u"valve_1_status")
        self.valve_1_status.setMaximumSize(QSize(16777215, 22))
        self.valve_1_status.setFont(font)
        self.valve_1_status.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.valve_1_status)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.valve_2_button = QPushButton(self.centralwidget)
        self.valve_2_button.setObjectName(u"valve_2_button")
        sizePolicy1.setHeightForWidth(self.valve_2_button.sizePolicy().hasHeightForWidth())
        self.valve_2_button.setSizePolicy(sizePolicy1)
        self.valve_2_button.setMinimumSize(QSize(100, 100))
        self.valve_2_button.setFont(font)
        self.valve_2_button.setCheckable(True)

        self.verticalLayout_3.addWidget(self.valve_2_button)

        self.valve_2_status = QLabel(self.centralwidget)
        self.valve_2_status.setObjectName(u"valve_2_status")
        self.valve_2_status.setMaximumSize(QSize(16777215, 22))
        self.valve_2_status.setFont(font)
        self.valve_2_status.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.valve_2_status)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.valve_3_button = QPushButton(self.centralwidget)
        self.valve_3_button.setObjectName(u"valve_3_button")
        sizePolicy1.setHeightForWidth(self.valve_3_button.sizePolicy().hasHeightForWidth())
        self.valve_3_button.setSizePolicy(sizePolicy1)
        self.valve_3_button.setMinimumSize(QSize(100, 100))
        self.valve_3_button.setFont(font)
        self.valve_3_button.setCheckable(True)

        self.verticalLayout_2.addWidget(self.valve_3_button)

        self.valve_3_status = QLabel(self.centralwidget)
        self.valve_3_status.setObjectName(u"valve_3_status")
        self.valve_3_status.setMaximumSize(QSize(16777215, 22))
        self.valve_3_status.setFont(font)
        self.valve_3_status.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.valve_3_status)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.valve_4_button = QPushButton(self.centralwidget)
        self.valve_4_button.setObjectName(u"valve_4_button")
        sizePolicy1.setHeightForWidth(self.valve_4_button.sizePolicy().hasHeightForWidth())
        self.valve_4_button.setSizePolicy(sizePolicy1)
        self.valve_4_button.setMinimumSize(QSize(100, 100))
        self.valve_4_button.setFont(font)
        self.valve_4_button.setCheckable(True)

        self.verticalLayout.addWidget(self.valve_4_button)

        self.valve_4_status = QLabel(self.centralwidget)
        self.valve_4_status.setObjectName(u"valve_4_status")
        self.valve_4_status.setMaximumSize(QSize(16777215, 22))
        self.valve_4_status.setFont(font)
        self.valve_4_status.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.valve_4_status)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.serial_stream = QLabel(self.centralwidget)
        self.serial_stream.setObjectName(u"serial_stream")
        self.serial_stream.setMaximumSize(QSize(16777215, 22))
        self.serial_stream.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.serial_stream)

        self.verticalLayout_5.setStretch(1, 1)

        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 725, 33))
        self.menuSerial = QMenu(self.menubar)
        self.menuSerial.setObjectName(u"menuSerial")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSerial.menuAction())
        self.menuFile.addAction(self.actionLoad_Positions)
        self.menuFile.addAction(self.actionSave_Positions)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionLoad_Positions.setText(QCoreApplication.translate("MainWindow", u"Load Positions", None))
        self.actionSave_Positions.setText(QCoreApplication.translate("MainWindow", u"Save Positions", None))
        self.position_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"Position 1", None))

        self.load_button.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.set_button.setText(QCoreApplication.translate("MainWindow", u"Set Item", None))
        self.add_item_button.setText(QCoreApplication.translate("MainWindow", u"Add Item", None))
        self.delete_item_button.setText(QCoreApplication.translate("MainWindow", u"Delete Item", None))
        self.close_all_button.setText(QCoreApplication.translate("MainWindow", u"Close All", None))
        self.valve_1_button.setText(QCoreApplication.translate("MainWindow", u"Valve 1", None))
        self.valve_1_status.setText(QCoreApplication.translate("MainWindow", u"Status: Closed", None))
        self.valve_2_button.setText(QCoreApplication.translate("MainWindow", u"Valve 2", None))
        self.valve_2_status.setText(QCoreApplication.translate("MainWindow", u"Status: Closed", None))
        self.valve_3_button.setText(QCoreApplication.translate("MainWindow", u"Valve 3", None))
        self.valve_3_status.setText(QCoreApplication.translate("MainWindow", u"Status: Closed", None))
        self.valve_4_button.setText(QCoreApplication.translate("MainWindow", u"Valve 4", None))
        self.valve_4_status.setText(QCoreApplication.translate("MainWindow", u"Status: Closed", None))
        self.serial_stream.setText(QCoreApplication.translate("MainWindow", u"Serial Stream: Disconnected", None))
        self.menuSerial.setTitle(QCoreApplication.translate("MainWindow", u"Serial", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

