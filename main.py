import time
import sys, os

import numpy as np
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from fuctions import taking_sorted_messages, select, click, message_count, sorted_text_list, set_driver_by
from bs4_code import req_url
from sort_all_messages import write_names_to_txt
from config import contact_list, archive, select_ico, argument1, argument2, chat
from folder_works import start_folder_work
from rename_files_names import start_renaming


# noinspection PyGlobalUndefined
def create_driver():
    options = webdriver.ChromeOptions();
    options.add_argument(argument1);
    options.add_argument(argument2)
    global driver, action
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://web.whatsapp.com")
    action = webdriver.ActionChains(driver)
    # send driver&By to fuctions.py
    set_driver_by(driver, By)


def choose_chat(ch=9, saved=9):
    group_dict = {0: 'park', 1: 'enb', 2: 'abai', 3: 'tbo'}
    # noinspection PyGlobalUndefined
    global group_flag, saved_number, group_name
    return_number = 0

    if (ch == 9) & (saved == 9):
        while True:
            try:
                group_flag = input("park-0, enb-1, abai-2, tbo-3: ")
                saved_number = input("0 - not saved numbers mes, 1 saved: ")
                group_flag, saved_number = int(group_flag), int(saved_number)
                if group_flag in [0, 1, 2, 3] and saved_number in [0, 1]:
                    group_name = group_dict[group_flag]
                    print("----------------------{}----------------------".format(group_name))
                    break
                else:
                    print('set one of 012')
            except:
                if 'stop' in [group_flag, saved_number]:
                    return_number = 1
                    break
                print('set only corrtect info')
        return return_number
    else:
        group_flag = ch
        saved_number = saved
        group_name = group_dict[group_flag]
        return return_number


def archive_open():
    print("Подождите")
    while True:  # waiting for wa
        try:
            select('//button[@class="{}"]', archive, "archive opened", clicked=1)
            break
        except:
            time.sleep(1)


def select_chat():
    select('//span[@title="{}"]', contact_list[group_flag],
           "contact opened", clicked=1)
    time.sleep(1)
    select('//span[@title="{}"]', contact_list[group_flag],
           "contact opened", clicked=1)
    time.sleep(2)


def find_mes_in_chat():
    # расчет сообщений -> меню -> выбор сообщений
    try:
        select('//span[@class="{}"]', "_3K42l", clicked=1)
    except:
        print("----------------------нет кнопки вниз----------------------")
    select('//div[@class="{}"]', '_28_W0', clicked=1)
    select('//div[@aria-label="{}"]', 'Выбрать сообщения', clicked=1)
    click()
    return message_count(group_flag, saved_number)


def select_messages():
    try:
        sorted_messages, sorted_messages_text, text_arr = taking_sorted_messages(saved_number=saved_number)
        # sorted_messages[i].text можно получить время отдельно
        txt_list = sorted_text_list()
        print('sm, smt, tm: ', len(sorted_messages), ' - ', len(sorted_messages_text), ' - ', len(txt_list))
        for text in txt_list:
            for j_text in sorted_messages_text:
                if text == str(j_text):
                    index = np.where(sorted_messages_text == text)[0][0]
                    try:
                        driver.execute_script("arguments[0].click();",
                                              sorted_messages.item(index).find_element(By.CLASS_NAME, select_ico))

                    except selenium.common.exceptions.NoSuchElementException:
                        if text.count(':') > 2:
                            action.move_to_element(sorted_messages.item(index)).perform()
                            driver.execute_script("arguments[0].click();",
                                                  sorted_messages.item(index).find_element(By.CLASS_NAME, select_ico))
                    sorted_messages_text = np.delete(sorted_messages_text, index)
                    sorted_messages = np.delete(sorted_messages, index)
                    break
        return text_arr
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno, e)


def downloadr_or_delete(text_arr):
    if saved_number == 1:
        print("----------------------names writen to sorted_messages_list.txt----------------------")
        name_lines = write_names_to_txt()
        try:
            select('//span[@data-testid="{}"]', class_name='download', clicked=1)
            while True:
                try:
                    time.sleep(2)
                    return start_renaming(group_name, start_folder_work(group_name), name_lines, text_arr)
                except Exception as e:
                    print('loop')
        except:
            select('//span[@data-testid="{}"]', class_name='x', clicked=1)

    else:
        try:
            select('//span[@data-testid="{}"]', class_name='delete', clicked=1)
            time.sleep(1.2)
            select('//div[@data-testid="{}"]', class_name='popup-controls-delete', clicked=1)
        except:
            select('//span[@data-testid="{}"]', class_name='x', clicked=1)
        return 0


def main(g=None, f=None):
    create_driver()
    archive_open()
    while True:
        try:
            input_text = input('wirte "stop" to stop the app: ')
            if input_text in ['0', '1', '2', '3']:
                control = choose_chat(int(input_text), 1)
            else:
                control = choose_chat()

            if control == 1:
                break
            else:
                if input_text == 'stop':
                    break
                time_begin = time.time()
                select_chat()
                if find_mes_in_chat() != 0:
                    text_arr = select_messages()
                else:
                    print('Нет сообщений для выделения')
                print('time for 1 role: ', time.time() - time_begin)
                # input()
                while True:
                    if downloadr_or_delete(text_arr) == 0:
                        break
                    else:
                        select('//div[@class="{}"]', '_28_W0', clicked=1)
                        select('//div[@aria-label="{}"]', 'Выбрать сообщения', clicked=1)
                        # вниз + find_mes
                        text_arr = select_messages()

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno, e)


if __name__ == "__main__":
    main()
    driver.quit()
