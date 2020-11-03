import pyautogui
import random
import time
import pytesseract
import cv2

# Download and install tesseract from
# https://github.com/UB-Mannheim/tesseract/wiki
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

plusButtonCenterLocation = pyautogui.locateCenterOnScreen('discord button.png')


def fish():
    message_on_discord('pls fish')
    read_and_type()


def hunt():
    message_on_discord('pls hunt')
    read_and_type()


def post_memes():
    message_on_discord('pls pm')
    meme_type = ['n', 'e', 'r', 'd']
    message_on_discord(random.choice(meme_type))


def beg():
    message_on_discord('pls beg')


def search():
    message_on_discord('pls search')
    read_text = screen_shot_and_read_text()
    search_this = read_text.split(',')
    eliminate = 'areaS1'
    if eliminate in search_this:
        search_this.remove(eliminate)
    if read_text.find("air") != -1:
        message_on_discord('air')
    else:
        message_on_discord(random.choice(search_this))


def sell():
    sell_random = ['boar', 'fish', 'duck', 'rabbit', 'skunk']
    message_on_discord('pls sell ' + random.choice(sell_random) + ' max')


def message_on_discord(command):
    pyautogui.click(plusButtonCenterLocation.x + 50,
                    plusButtonCenterLocation.y)
    pyautogui.typewrite(command)
    pyautogui.typewrite(['enter'])
    time.sleep(5)


def dep():
    message_on_discord('pls dep max')


# def join_heist():
# Join them by typing JOIN HEIST in the next 90 seconds


def read_and_type():
    read_text = screen_shot_and_read_text()
    print(read_text)
    if read_text.find("Type") != -1:
        type_input = read_text.split('Type ', 1)[1]
        message_on_discord(type_input)


def screen_shot_and_read_text():
    pyautogui.screenshot(region=(plusButtonCenterLocation.x + 25,
                                 plusButtonCenterLocation.y - 64, 500, 20),
                         imageFilename='screen_shot.png')
    img = cv2.imread('screen_shot.png')
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.bitwise_not(gray_img)
    read_text = pytesseract.image_to_string(img, lang='eng')
    read_text = read_text.replace('', '')
    return read_text


def detect_button():
    if str(plusButtonCenterLocation) == 'None':
        print("Unable to detect discord message input")
        return False
    else:
        return True
