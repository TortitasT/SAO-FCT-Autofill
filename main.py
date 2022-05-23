from asyncore import write
from calendar import week
from multiprocessing.connection import wait
import pyautogui
import time
import pyperclip
import random
import requests
from requests.structures import CaseInsensitiveDict
from dotenv import load_dotenv
from dotenv import dotenv_values

load_dotenv()
env = dotenv_values(".env")

weekDates = [
    '21%2F03%2F2022-27%2F03%2F2022',
    '28%2F03%2F2022-03%2F04%2F2022',
    '04%2F04%2F2022-10%2F04%2F2022',
    '11%2F04%2F2022-17%2F04%2F2022',
    '18%2F04%2F2022-24%2F04%2F2022',
    '25%2F04%2F2022-01%2F05%2F2022',
    '02%2F05%2F2022-08%2F05%2F2022',
    '09%2F05%2F2022-15%2F05%2F2022',
    '16%2F05%2F2022-22%2F05%2F2022',
    '23%2F05%2F2022-29%2F05%2F2022',
    '30%2F05%2F2022-03%2F06%2F2022',
]

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

autocomplete = input("Do you want to autocomplete your diary? (y/n): ")
if autocomplete == 'y':
    autocomplete = True

    weeks = int(input("How many weeks?: "))
    while not weeks:
        weeks = int(input("How many weeks?: "))

    isMacOS = input("Is this a MacOS keyboard? (y/n): ")
    if isMacOS == 'y':
        isMacOS = True
    else:
        isMacOS = False
else:
    autocomplete = False

export = input("Do you want to export to pdf? (This requires session id in .env) (y/n): ")
if export == 'y':
    export = True
else:
    export = False

if autocomplete:
    
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
        
        # Go to next week
        selector = "this.document.querySelector('.celdaInfoAlumno').childNodes[5].click()"
        pastewrite(selector)
        pyautogui.press("enter")

        time.sleep(0.1)

    pyautogui.press("f12")

if export:
    print("Exporting to pdf...")

    for i in range(11):
        try:
            url = "https://fct.edu.gva.es/inc/ajax/generar_pdf.php?doc=5&idFct={}&centro={}&semanaDiario={}".format(env['IDFCT'], env['CENTER'], weekDates[i])

            headers = CaseInsensitiveDict()

            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive",
                "Cookie": "_ga=GA1.2.991372322.1631818129; __utma=192432508.991372322.1631818129.1635672972.1635672972.1; ZDEDebuggerPresent=php,phtml,php3; BIGipServerP_WEBEDU={}; PHPSESSID={}".format(env['BIGipServerP_WEBEDU'], env['PHPSESSID']),
                "Upgrade-Insecure-Requests": "1",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
            }


            resp = requests.get(url, headers=headers, stream=True)

            if(resp.status_code != 200):
                raise Exception("Response failed") 

            write_path = "week{}.pdf".format(i+1)

            with open(write_path, 'wb') as f:
                f.write(resp.content)
        except Exception as e:
            print(e)
            print("Error exporting week {}".format(i+1))
            continue
