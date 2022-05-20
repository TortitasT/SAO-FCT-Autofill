import pyautogui
import time
import pyperclip
import random
import requests

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

isMacOS = input("Is this a MacOS keyboard? (y/n)")
if isMacOS == 'y':
    isMacOS = True
else:
    isMacOS = False

export = input("Do you want to export to pdf? (y/n)")
if export == 'y':
    export = True
else:
    export = False

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

    # Export to pdf
    # if export:
    #     selector = "document.querySelectorAll('.botonform')[1].click()"
    #     pastewrite(selector.format(i))
    #     pyautogui.press("enter")

    #     time.sleep(1)
    #     pyautogui.press("f12")
    #     time.sleep(0.5)

        # TODO ❯ curl 'https://fct.edu.gva.es/inc/ajax/generar_pdf.php?doc=5&idFct=978096&centro=43&semanaDiario=21%2F03%2F2022-27%2F03%2F2022' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:100.0) Gecko/20100101 Firefox/100.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8' -H 'Accept-Language: es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3' -H 'Accept-Encoding: gzip, deflate, br' -H 'Connection: keep-alive' -H 'Cookie: f5_cspm=1234; BIGipServerP_WEBEDU=1585848236.20480.0000; ZDEDebuggerPresent=php,phtml,php3; PHPSESSID=session id' -H 'Upgrade-Insecure-Requests: 1' -H 'Sec-Fetch-Dest: document' -H 'Sec-Fetch-Mode: navigate' -H 'Sec-Fetch-Site: same-origin' -H 'If-Modified-Since: Fri, 20 May 2022 11:55:42 GMT' --output test.pdf

    
    # Go to next week
    selector = "this.document.querySelector('.celdaInfoAlumno').childNodes[5].click()"
    pastewrite(selector)
    pyautogui.press("enter")

    time.sleep(0.1)

pyautogui.press("f12")
print("Done!")

if export:
    print("Exporting to pdf...")
    startWeek = int(input("How many weeks?"))
    while not startWeek:
        startWeek = int(input("How many weeks?"))

    for i in range(startWeek, weeks):
        
