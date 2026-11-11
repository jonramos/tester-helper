import random
import tkinter as tk

import pystray
from pynput import keyboard
from PIL import Image, ImageDraw


def generate_cpf():
    digits = [random.randint(0, 9) for _ in range(9)]

    def checksum(base_digits):
        total = sum(
            digit * weight
            for digit, weight in zip(base_digits, range(len(base_digits) + 1, 1, -1))
        )
        result = 11 - (total % 11)
        return 0 if result >= 10 else result

    first_digit = checksum(digits)
    second_digit = checksum(digits + [first_digit])
    cpf_digits = digits + [first_digit, second_digit]
    cpf = ''.join(str(digit) for digit in cpf_digits)
    formatted_cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    print(formatted_cpf)
    copy_to_clipboard(formatted_cpf)
    return formatted_cpf

def generate_cnpj():
    digits = [random.randint(0, 9) for _ in range(12)]

    def checksum(base_digits):
        weights = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        total = sum(digit * weight for digit, weight in zip(base_digits, weights))
        result = total % 11
        return 0 if result < 2 else 11 - result

    first_digit = checksum(digits)
    second_digit = checksum(digits + [first_digit])
    cnpj_digits = digits + [first_digit, second_digit]
    cnpj = ''.join(str(digit) for digit in cnpj_digits)
    formatted_cnpj = f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"
    print(formatted_cnpj)
    copy_to_clipboard(formatted_cnpj)
    return formatted_cnpj

def copy_to_clipboard(text):
    root = tk.Tk()
    root.withdraw()
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()
    root.destroy()


# Helper function to generate a simple colored icon dynamically
def create_image():
    # Creates a 64x64 image with a blue "T" letter
    image = Image.new('RGB', (64, 64), (0, 0, 0))
    dc = ImageDraw.Draw(image)
    dc.rectangle((26, 14, 38, 50), fill=(0, 120, 215))
    dc.rectangle((14, 14, 50, 22), fill=(0, 120, 215))
    return image


def on_cpf_hotkey():
    generate_cpf()


def on_cnpj_hotkey():
    generate_cnpj()

def on_clicked(icon, item):
    if item.text == "Generate CPF":
        generate_cpf()
    elif item.text == "Generate CNPJ":
        generate_cnpj()
    elif item.text == "Exit":
        if 'shortcut' in globals() and shortcut is not None:
            shortcut.stop()
        icon.stop()


def start_global_shortcut():
    hotkeys = keyboard.GlobalHotKeys({
        '<ctrl>+1': on_cpf_hotkey,
        '<ctrl>+2': on_cnpj_hotkey,
    })
    hotkeys.start()
    return hotkeys


# Set up the icon and context menu
icon = pystray.Icon(
    "TesterHelper",
    create_image(),
    "Tester Helper",
    menu=pystray.Menu(
        pystray.MenuItem("Generate CPF", on_clicked),
        pystray.MenuItem("Generate CNPJ", on_clicked),
        pystray.Menu.SEPARATOR,
        pystray.MenuItem("Exit", on_clicked)
    )
)

#shortcut = None

if __name__ == "__main__":
    shortcut = start_global_shortcut()
    icon.run()