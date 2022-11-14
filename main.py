import time
import sys, os
# import requests
import pyautogui as pg
# from lxml import etree, html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fuctions import taking_sorted_messages, select, write_to_file, click, \
    message_count, sorted_text_list, set_driver_by
from bs4_code import req_url
from test import start_park_rename
from config import contact, archive, select_ico, argument1, argument2, msg_cont_class, chat


def create_driver():
    options = webdriver.ChromeOptions();
    options.add_argument(argument1);
    options.add_argument(argument2)
    global driver
    global action
    driver = webdriver.Chrome \
        (executable_path=r'C:\Users\OFFICE\PycharmProjects\whatsapp-project\stuf\chromedriver.exe',
         options=options)
    driver.get("https://web.whatsapp.com")
    action = webdriver.ActionChains(driver)
    # send driver&By to fuctions.py
    set_driver_by(driver, By)


def choose_chat():
    global group_flag, saved_number
    while True:
        try:
            group_flag = int(input("park-0, enb-1, abai-2: "))
            saved_number = int(input("0 - not saved numbers mes, 1 saved: "))
            if group_flag in [0, 1, 2] and saved_number in [0, 1]:
                print("Selected {}".format(group_flag))
                break
            else:
                print('set one of 012')
        except:
            print('set only corrtect info')


def select_chat():
    select('//span[@title="{}"]', contact[group_flag], "contact opened", clicked=1)


def archive_open():
    print("Подождите")
    while True:  # waiting for wa
        try:
            select('//button[@class="{}"]', archive, "archive opened", clicked=1)
            break
        except:
            time.sleep(1)


def find_mes_in_chat():
    # расчет сообщений -> меню -> выбор сообщений
    try:
        select('//span[@class="{}"]',"_3K42l", clicked=1)
    except:
        print('нет кнопки вниз')
    click()
    return message_count(group_flag, saved_number)


def select_messages():
    select('//div[@class="{}"]', '_28_W0', clicked=1)
    select('//div[@aria-label="{}"]', 'Выбрать сообщения', clicked=1)
    sorted_messages = taking_sorted_messages(saved_number=saved_number)
    txt_list = sorted_text_list()
    print('len sorted_m: ', len(sorted_messages))
    time_a = time.time()
    for mes in sorted_messages:
        j_text = str(''.join(''.join(mes.text.splitlines())))
        if j_text in txt_list:
            try:

                driver.execute_script("arguments[0].click();",
                                      mes.find_element(By.CLASS_NAME, select_ico))
            except Exception as e:
                if j_text.count(':') > 2:
                    action.move_to_element(mes).perform()
                driver.execute_script("arguments[0].click();",
                                      mes.find_element(By.CLASS_NAME, select_ico))
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
            txt_list.remove(j_text)
    print(time.time() - time_a)


def main():
    create_driver()
    archive_open()
    while input('wirte "stop" to stop the app: ') != 'stop':
        input_text = ''
        time_begin = time.time()
        choose_chat()
        select_chat()
        time.sleep(5)
        try:
            if find_mes_in_chat() != 0:
                select_messages()
            else:
                print('Нет сообщений для выделения')
            print("------------------------------------------")
        except Exception as e:
            print('main-103: ', e)
        print('time for 1 role: ', time_begin - time.time())
        print('input_text: ')

        while input_text not in ['close']:
            print('-------  -------  Доп функцийй  -------  -------')
            input_text = str(input('print "close" to close this window: ')).lower()
            if input_text == 'take names':
                print("names writen to park mes name")
                start_park_rename()
            elif input_text == 'download':
                select('//span[@data-testid="{}"]', class_name='download', clicked=1)
            elif input_text == 'help':
                print("""
                download
                take names
                close
                stop
                """)
        print('-------  -------  -------  -------  -------  -------')


if __name__ == "__main__":
    main()


input()
driver.quit()
