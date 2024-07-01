import random
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
import sys
from selenium.webdriver.chrome.options import Options

class colors:
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CBLACK = '\33[30m'
    CRED = '\33[31m'
    CGREEN = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE = '\33[36m'
    CWHITE = '\33[37m'

color_random = [colors.CBLUE, colors.CVIOLET, colors.CWHITE, colors.OKBLUE, colors.CGREEN, colors.WARNING,
                colors.CRED, colors.CBEIGE]
random.shuffle(color_random)

def entryy():
    x = color_random[0] + """
     
  _  __    _              _           __  _____ ___  
 | |/ /___| |_ __ _ _ __ (_)_ _  ___  \ \/ / __/ __| 
 | ' </ -_)  _/ _` | '  \| | ' \/ -_)  >  <\__ \__ \ 
 |_|\_\___|\__\__,_|_|_|_|_|_||_\___| /_/\_\___/___/ 
                                                     
      XSS Scanner           
      Coded by Ilya Koslov      
      Instagram ==> ilya.koslof 
\n"""
    for c in x:
        print(c, end='')
        sys.stdout.flush()
        sleep(0.0045)
    oo = " " * 6 + 29 * "░⣿" + "\n\n"
    for c in oo:
        print(colors.CGREEN + c, end='')
        sys.stdout.flush()
        sleep(0.0065)

    tt = " " * 6 + "░⣿" + " " * 18 + "Welcome to Ketamine XSS Scanner" + " " * 11 + "░⣿" + "\n\n"
    for c in tt:
        print(colors.CWHITE + c, end='')
        sys.stdout.flush()
        sleep(0.0065)
    xx = " " * 6 + 29 * "░⣿" + "\n\n"
    for c in xx:
        print(colors.CGREEN + c, end='')
        sys.stdout.flush()
        sleep(0.0065)

def xssInj(c):
    print("Trying payloads list, Please wait...")
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    browser = webdriver.Chrome(options=chrome_options)
    browser.maximize_window()
    count = 0
    with open("myfile.txt", "r", encoding="UTF-8") as file:
        a = file.readlines()
        try:
            while count < len(a):
                url_to_visit = c.strip() + a[count].strip()  # Strip whitespace and concatenate
                print("Testing: " + url_to_visit)
                browser.get(url_to_visit)
                sleep(random.randint(1, 3))
                count += 1
                if count == len(a):
                    browser.close()
        except UnexpectedAlertPresentException:
            print(colors.CRED + "Successful Payload==>", a[count - 1])
            print("Url==>" + url_to_visit)
            sleep(5)
            browser.quit()
        except Exception as exc:
            print(f"Thread error: {exc}")
            browser.quit()

if __name__ == "__main__":
    entryy()
    target_site = input("Enter URL: ")
    xssInj(target_site)
