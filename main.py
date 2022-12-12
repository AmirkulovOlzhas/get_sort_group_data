import time
import sys, os
import pyautogui as pg
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fuctions import taking_sorted_messages, select, write_to_file, click, \
    message_count, sorted_text_list, set_driver_by
from bs4_code import req_url
from sort_all_messages import write_names_to_txt
from config import contact_list, archive, select_ico, argument1, argument2, msg_cont_class, chat
from folder_works import start_folder_work
from rename_files_names import start_renaming


# noinspection PyGlobalUndefined
def create_driver():
    options = webdriver.ChromeOptions();
    options.add_argument(argument1);
    options.add_argument(argument2)
    global driver, action
    driver = webdriver.Chrome \
        (executable_path=r'C:\Users\OFFICE\PycharmProjects\whatsapp-project\stuf\chromedriver.exe',
         options=options)
    driver.get("https://web.whatsapp.com")
    action = webdriver.ActionChains(driver)
    # send driver&By to fuctions.py
    set_driver_by(driver, By)


def choose_chat():
    group_dict = {0: 'park', 1: 'enb', 2: 'abai', 3: 'tbo'}
    # noinspection PyGlobalUndefined
    global group_flag, saved_number, group_name
    return_number = 0

    while True:
        try:
            group_flag = input("park-0, enb-1, abai-2, tbo-3: ")
            saved_number = input("0 - not saved numbers mes, 1 saved: ")
            group_flag, saved_number = int(group_flag), int(saved_number)
            if group_flag in [0, 1, 2, 3] and saved_number in [0, 1]:
                print("Selected {}".format(group_flag))
                group_name = group_dict[group_flag]
                break
            else:
                print('set one of 012')
        except:
            if 'stop' in [group_flag, saved_number]:
                return_number = 1
                break
            elif 'skip' in [group_flag, saved_number]:
                return_number = 2
                break
            print('set only corrtect info')
    return return_number


def select_chat():
    select('//span[@title="{}"]', contact_list[group_flag], "contact opened", clicked=1)
    time.sleep(2)


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
        select('//span[@class="{}"]', "_3K42l", clicked=1)
    except:
        print('нет кнопки вниз')
    click()
    return message_count(group_flag, saved_number)


def select_messages():
    try:
        select('//div[@class="{}"]', '_28_W0', clicked=1)
        select('//div[@aria-label="{}"]', 'Выбрать сообщения', clicked=1)
        time_88 = time.time()
        sorted_messages, sorted_messages_text = taking_sorted_messages(saved_number=saved_number)
        time_89 = time.time()
        txt_list = sorted_text_list()
        print('91: ', time.time()-time_89, '\n88: ', time.time()-time_88)
        print('len sorted_m, txt_mes: ', len(sorted_messages), ' - ', len(txt_list))
        time_a = time.time()

        for text in txt_list:
            for j_text in sorted_messages_text:
                if text == str(j_text):
                    index = sorted_messages_text.index(text)
                    try:
                        driver.execute_script("arguments[0].click();",
                                              sorted_messages[index].find_element(By.CLASS_NAME, select_ico))

                    except selenium.common.exceptions.NoSuchElementException:
                        # if text.count(':') > 2:
                        action.move_to_element(sorted_messages[index]).perform()
                        driver.execute_script("arguments[0].click();",
                                              sorted_messages[index].find_element(By.CLASS_NAME, select_ico))
                    sorted_messages_text.remove(j_text)
                    sorted_messages.remove(sorted_messages[index])
                    break
        print(time.time() - time_a)
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno, e)


def downloadr_or_delete():
    if saved_number == 1:
        print("names writen to park mes name")
        write_names_to_txt()
        try:
            select('//span[@data-testid="{}"]', class_name='download', clicked=1)
            time.sleep(7)
            while True:
                try:
                    start_renaming(group_name, start_folder_work(group_name))
                    break
                except Exception as e:
                    time.sleep(2)
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

def main():
    create_driver()
    archive_open()
    while True:
        try:
            input_text = input('wirte "stop" to stop the app: ')
            control = choose_chat()
            if control == 1:
                break
            elif control == 2:
                print('skiped')
            else:

                if input_text != 'skip':
                    time_begin = time.time()
                    select_chat()
                    if find_mes_in_chat() != 0:
                        select_messages()
                    else:
                        print('Нет сообщений для выделения')
                    print('time for 1 role: ', time.time() - time_begin)
                    downloadr_or_delete()
                elif input_text == 'stop':
                    break
                else:
                    while input_text != 'close':
                        print('-------  -------  Доп функцийй  -------  -------')
                        input_text = str(input('print "close" to close this window: ')).lower()
                        if input_text == 'rename':
                            try:
                                start_renaming(group_name, start_folder_work(group_name))
                            except IndexError:
                                print('was downloaded wrong')
                    print('-------  -------  -------  -------  -------  -------')

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno, e)


if __name__ == "__main__":
    main()

input()
driver.quit()
