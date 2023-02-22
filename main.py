import os
import sys
import time

import numpy as np
import selenium.common.exceptions
from config import contact_list, archive, select_ico, argument1, argument2
from folder_works import start_folder_work
from fuctions import taking_sorted_messages, select, click, message_count, set_driver_by
from rename_files_names import start_renaming
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from sort_all_messages import write_names_to_txt
from webdriver_manager.chrome import ChromeDriverManager


# noinspection PyGlobalUndefined
def create_driver():
    options = webdriver.ChromeOptions()
    options.add_argument(argument1)
    options.add_argument(argument2)
    global driver, action
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://web.whatsapp.com")
    action = webdriver.ActionChains(driver)
    # send driver&By to functions.py
    set_driver_by(driver, By)


def choose_chat(ch=None, saved=9):
    group_dict = {0: 'park', 1: 'enb', 2: 'turan', 3: 'tbo', 4: 'karatau', 5: 'ТБО, Туран, Азат, Мирас', 6: 'ТБО ГОРОД',
                  7: 'Больница РОЩА', 9: 'None'}
    # noinspection PyGlobalUndefined
    global group_flag, saved_number
    return_number = 0

    if (ch == None) & (saved == 9):
        while True:
            try:
                for i in range(4):
                    print(f'{i} - {contact_list[i]}')
                group_flag = input()
                saved_number = input("0 - not saved numbers mes, 1 saved: ")
                group_flag, saved_number = int(group_flag), int(saved_number)
                if group_flag in [0, 1, 2, 3, 4, 5, 6, 7] and saved_number in [0, 1, 3, 2]:
                    print("----------------------{}----------------------".format(group_dict[group_flag]))
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
        return return_number


def archive_open():
    print("Подождите")
    while True:  # waiting for wa
        try:
            select('//button[@class="{}"]', archive, clicked=1)
            break
        except:
            time.sleep(1)


def select_chat():
    select('//span[@title="{}"]', contact_list[group_flag], clicked=1)
    time.sleep(1)
    select('//span[@title="{}"]', contact_list[group_flag], clicked=1)
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
    return message_count()


def select_messages():
    sorted_messages, sorted_messages_text, text_arr = taking_sorted_messages(saved_number=saved_number,
                                                                             contact=group_flag)
    print('sm, smt, tm: ', len(sorted_messages), ' - ', len(sorted_messages_text))
    if 'Сообщения' == sorted_messages_text[0][0][:9]:
        sorted_messages_text = sorted_messages_text[1:]
        sorted_messages = np.delete(sorted_messages, 0)
    for m in sorted_messages:
        try:
            driver.execute_script("arguments[0].click();",
                                  m.find_element(By.CLASS_NAME, select_ico))
        except selenium.common.exceptions.NoSuchElementException:
            try:
                action.move_to_element(m).perform()
                driver.execute_script("arguments[0].click();",
                                      m.find_element(By.CLASS_NAME, select_ico))
            except:
                pass
            break
    return text_arr, sorted_messages_text


def find_select():
    if find_mes_in_chat() != 0:
        text_arr, smt = select_messages()
        return text_arr, smt
    else:
        return 0, []


def download_or_delete(text_arr, smt):
    if saved_number in [1, 3]:
        print("----------------------names saved----------------------")
        select('//span[@data-testid="{}"]', class_name='download', clicked=1)
        name_lines = write_names_to_txt(smt)
        while True:
            try:
                return start_renaming(start_folder_work(group_flag), name_lines, text_arr, group_flag)
            except:
                time.sleep(2)
    else:
        input()
        select('//span[@data-testid="{}"]', class_name='delete', clicked=1)
        time.sleep(1.2)
        select('//div[@data-testid="{}"]', class_name='popup-controls-delete', clicked=1)
        return 0


def main():
    # открывает хром
    create_driver()
    archive_open()
    # цикл действий
    while True:
        try:
            input_text = input('wirte "stop" to stop the app: ')
            if input_text in ['0', '1', '2', '3', '4']:
                control = choose_chat(int(input_text), 1)
            # загрузка фото выбранного чата
            elif input_text.lower() == 'start':
                try:
                    temp_g_name = driver.find_element(By.XPATH,
                                                      '//span[@data-testid="conversation-info-header-chat-title"]').text
                except:
                    temp_g_name = '???'
                control = choose_chat(temp_g_name, 3)

            else:
                control = choose_chat()

            if control == 1:
                break
                # pass
            else:
                if input_text == 'stop':
                    break
                time_begin = time.time()
                if isinstance(group_flag, int):
                    select_chat()
                #select chat by chat name
                text_arr, smt = find_select()
                print('time for 1 role: ', time.time() - time_begin)
                if type(text_arr) != "<class 'int'>":
                    # input()
                    while True:
                        if download_or_delete(text_arr, smt) == 0:
                            break
                        else:
                            # вниз + find_mes + если соообщений нет
                            text_arr, smt = find_select()
                    if saved_number in [1, 3]:
                        if input('Очистить чат? (y/n) или (да/нет)').lower() in ['y', 'да']:
                            select('//div[@class="{}"]', '_28_W0', clicked=1)
                            select('//div[@aria-label="{}"]', 'Очистить чат', clicked=1)
                            select('//div[@class="{}"]', "_1M6AF _3QJHf", clicked=1)

                else:
                    print('Нет сообщений для скачивания')
                    select('//button[@aria-label="{}"]', class_name='Отменить пересылку', clicked=1)

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno, e)


if __name__ == "__main__":
    main()
    driver.quit()
