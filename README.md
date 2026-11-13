# Tester Helper

This project uses a few Python packages to create a system tray app with a global keyboard shortcut.


## Dependences
```bash
python -m pip install --upgrade pip
python -m pip install pystray pynput pillow pyperclip
```

## Run

```bash
python main.py
```

## Keyboard shortcuts

- Ctrl+1: Generate a CPF
- Ctrl+2: Generate a numeric CNPJ
- Ctrl+3: Generate an alphanumeric CNPJ

## Dependency summary

- pystray: Creates the system tray icon and menu
- pynput: Handles the global keyboard shortcut
- Pillow: Generates the tray icon image
