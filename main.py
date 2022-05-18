import pyautogui
import time
import pyperclip
import random

isMacOS = False
def commandKey():
    """
    Returns the command key for the current keyboard layout.
    """
    if isMacOS:
        return 'command'
    else:
        return 'ctrl'

def pastewrite(text):
    """
    This is a work-around for the bug in pyautogui.write() with non-QWERTY keyboards
    It copies the text to clipboard and pastes it, instead of typing it.
    """
    pyperclip.copy(text)
    pyautogui.hotkey(commandKey(), 'v')
    pyperclip.copy('')

descriptions = open('descriptions.txt').read().splitlines()
def rngDescription():
    """
    Generates a random description for the item.
    """
    return random.choice(descriptions)

# BEGIN

print("Welcome to FCT SAO auto-filler :)")

weeks = int(input("How many weeks?"))
while not weeks:
    weeks = int(input("How many weeks?"))

isMacOSInput = input("Is this a MacOS keyboard? (y/n)")
if isMacOSInput == 'y':
    isMacOS = True

print("Starting in 5 seconds, go to week 1 page and stay still...")

time.sleep(5)
pyautogui.press("f5")
pyautogui.press("enter")
time.sleep(1)
pyautogui.press("f12")
time.sleep(0.5)
pyautogui.hotkey(commandKey(), 'alt', 'k')
time.sleep(0.5)

for i in range(weeks):
    time.sleep(2)

    print('Editing week {}...'.format(i+1))

    for i in range(5):
        print('Editing day {} of the week...'.format(i+1))

        selector = "document.getElementById('modificar{}').click();"
        pastewrite(selector.format(i))
        pyautogui.press("enter")

        time.sleep(0.1)

        selector = "document.getElementById('descripcion{}').value = '{}';"
        pastewrite(selector.format(i, rngDescription()))
        pyautogui.press("enter")

        time.sleep(0.1)

        selector = "document.getElementById('tiempo{}').value = 8;"
        pastewrite(selector.format(i))
        pyautogui.press("enter")

        time.sleep(0.1)

        selector = "document.getElementById('aceptar{}').click()"
        pastewrite(selector.format(i))
        pyautogui.press("enter")

        time.sleep(0.1)
    
    selector = "this.document.querySelector('.celdaInfoAlumno').childNodes[5].click()"
    pastewrite(selector)
    pyautogui.press("enter")

    time.sleep(0.1)

pyautogui.press("f12")
print("Done!")
