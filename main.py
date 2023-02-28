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


def choose_chat(ch=None, saved=99):
    # noinspection PyGlobalUndefined
    global group_flag, saved_number
    group_flag = None
    saved_number = None
    return_number = 0

    if (ch == None) & (saved == 99):
        while True:
            try:
                for i in range(len(contact_list)):
                    print(f'{i} - {contact_list[i]}')
                group_flag = input()
                saved_number = input("0 - выбор фото и сообщений не сохраненных контактов, "
                                     "1 - загрузка фото и сообщений сохраненных"
                                     "2 - выбор всех сообщений"
                                     "3 - сохранение фото и текста всех контактов: ")
                group_flag, saved_number = int(group_flag), int(saved_number)
                if group_flag in range(len(contact_list)) and saved_number in [0, 1, 3, 2]:
                    print("----------------------{}----------------------".format(contact_list[group_flag]))
                    break
                else:
                    print('введите корректное число')
            except Exception as e:
                if 'stop' in [group_flag, saved_number]:
                    return_number = 1
                    break
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno, e)
                print('Введи числа')
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
        select('//span[@class="{}"]', "_3K42l", clicked=1)  # кнопка вниз
    except:
        print("----------------------нет кнопки вниз----------------------")
    select('//div[@class="{}"]', '_28_W0', clicked=1)  # три точки
    select('//div[@aria-label="{}"]', 'Выбрать сообщения', clicked=1)  # выбор сообщений
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


def download_or_delete(text_arr, smt, auto_delete):
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


def main(contact=None, sn=None):
    while True:
        try:
            if contact is None:
                auto_delete = 0
                input_text = input('1 - Пункт.'
                                   'Введите от 0-8 что бы сохранить фото от сохраненных контактов группы\n'
                                   'либо вручную откройте группу и напишете "start" чтобы сохранить все \n'
                                   'что бы сделать расширенный выбор, введите пустую строку: ')
                if input_text in ['0', '1', '2', '3', '4', '5', '6', '7', '8']:
                    control = choose_chat(int(input_text), 1)
                # загрузка фото выбранного чата
                elif input_text.lower() == 'start':
                    try:
                        temp_g_name = driver.find_element(By.XPATH,
                                                          '//span[@data-testid="conversation-info-header-chat-title"]').text
                    except:
                        temp_g_name = '???'
                    control = choose_chat(temp_g_name, 3)
                elif input_text == 'stop':
                    break
                else:
                    control = choose_chat()
            else:
                auto_delete = 1
                input_text = ''
                control = choose_chat(contact, sn)

            if control == 1:
                break
                # pass
            else:
                if input_text == 'stop':
                    break
                time_begin = time.time()
                if isinstance(group_flag, int):
                    select_chat()
                # select chat by chat name
                try:
                    text_arr, smt = find_select()
                except:
                    print('Нет сообщений!')
                    break
                print('time for 1 role: ', time.time() - time_begin)
                if type(text_arr) != "<class 'int'>":
                    # input()
                    while True:
                        if download_or_delete(text_arr, smt, auto_delete) == 0:
                            break
                        else:
                            # вниз + find_mes + если соообщений нет
                            text_arr, smt = find_select()
                    # if saved_number in [1, 3]:
                    #     if input('Очистить чат? (y/n) или (да/нет)').lower() in ['y', 'да']:
                    try:
                        if auto_delete:
                            x = 1
                        else:
                            if input('Очистить чат? (y/n) или (да/нет)').lower() in ['y', 'да']:
                                x = 1
                            else:
                                x = 0
                        if x:
                            select('//div[@class="{}"]', '_28_W0', clicked=1)
                            select('//div[@aria-label="{}"]', 'Очистить чат', clicked=1)
                            time.sleep(2)
                            select('//div[@class="{}"]', "_1M6AF _3QJHf", clicked=1)
                            time.sleep(2)
                            select('//div[@class="{}"]', "_1M6AF _3QJHf", clicked=1)
                            time.sleep(5)
                    except:
                        print('Сообщения не удалены')

                else:
                    print('Нет сообщений для скачивания')
                    select('//button[@aria-label="{}"]', class_name='Отменить пересылку', clicked=1)
                break

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno, e)


if __name__ == "__main__":
    list_of_group = [
        [0, 1], [1, 1], [2, 1],
        [3, 3], [4, 3], [5, 3],
        [6, 3], [7, 3]  # , [8, 3]
    ]
    create_driver()
    archive_open()
    for i in list_of_group:
        select('//span[@title="{}"]', contact_list[i[0]], clicked=1)
        time.sleep(1.5)
    # main()
    for i in list_of_group:
        # открывает хром
        if i[0] == 3:
            driver.quit()
            create_driver()
            archive_open()
        # цикл действий
        print(f'-----------------{i}------------------')
        try:
            main(i[0], i[1])
        except:
            pass
    driver.quit()
