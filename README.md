# Valve Controller

Windows/Linux GUI for the serial valve controller.

```
git clone <repo-url> && cd <repo>
uv sync
uv run valve-controller
```

Pumps/valves need not be connected: the GUI opens regardless. Use **Serial → Refresh Devices** (F5) after plugging in.
On Linux you may need serial access: `sudo usermod -aG uucp,dialout $USER` (re-login).
