import os
import sys
import time

import numpy as np
import pyautogui as pg
from bs4_code import req_url
from config import chat, not_select_messages


# noinspection PyGlobalUndefined
def set_driver_by(d, B):
    global driver
    global By
    driver, By = d, B


def click(click_c=1):
    for i in range(click_c):
        pg.click(389, 777, button='middle')


def split_text_date(td):
    try:
        ti = td.index(':')
        date = td[ti - 2:ti + 3]
        text = td[:ti - 2]
        text = text.replace('Пересланное сообщение', '')
        text = text.replace('Данное сообщение удалено', '')
        while '**' in text:
            try:
                text = text.split('**')[1]
            except:
                text = ''
        if text:
            if date[0] not in ['е', 'в', '4', '5', '6', '7', '8', '9']:
                print(end='.')
                s = date + '-' + text + '\n'
                return s
    except:
        pass


def taking_sorted_messages(saved_number=0, contact=0):
    a = time.time()
    time_sum = 0
    messages = np.array(driver.find_element(
        By.XPATH, '//div[@class="{}"]'.format(chat)). \
                        find_elements(By.XPATH, '//div[@data-id]'))
    sm, smt = np.array([]), []
    if saved_number:
        text_arr = np.array([])
        messages_classes = np.array(driver.find_element(
            By.XPATH, '//div[@class="{}"]'.format(chat)). \
                                    find_elements(By.XPATH, '//div[@data-id]//div[contains(@class, "_1-lf9")]'))
        for i in range(len(messages)):
            try:
                m = messages[i].text.splitlines()
                b = time.time()
                text_date = ''.join(m)
                # print('-', '---'.join(m))
                time_sum += time.time() - b
                mes_class = messages_classes[i].get_attribute("class")
                mes_class = np.array(mes_class.split())
                # not_select_mess
                if '+7 7' not in text_date:
                    if all(bad_class not in mes_class for bad_class in not_select_messages):
                        sm = np.append(sm, messages[i])
                        smt.append(m)  # text_date
                    if len(text_date.split(':')[0]) > 2:
                        # Тараз мкр11:55
                        text_arr = np.append(text_arr, split_text_date(text_date))
                    mes_class = None
            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno, e)
        if 'Сообщения защищены' in smt[0][0]:  # smt[0]
            sm = np.delete(sm, 0)
            smt.remove(smt[0])
        messages = messages_classes = None
        print('\n-------------------------------\ntime for tsm: ', time.time() - a, ' - ', time_sum,
              '\n-----------------------------------')
        return sm, smt, text_arr
    else:
        for mes in messages:
            m = mes.text.splitlines()
            #
            if len(m) > 1:
                temp_value = None
                if contact == 1:
                    temp_value = 'Енб-'
                elif contact == 2:
                    temp_value = 'Абай'
                if temp_value:
                    if ''.join(m)[0:4] not in ['Абай', 'Енб-']:
                        # print('-', '---'.join(mes.text.splitlines()))
                        smt.append(m)  # temp
                        sm = np.append(sm, mes)
                else:
                    smt.append(m)  # temp
                    sm = np.append(sm, mes)

        return sm, smt, []


def select(xpath, class_name, clicked=0):
    selected_element = driver.find_element(By.XPATH, xpath.format(class_name))
    if clicked == 1:
        selected_element.click()
    time.sleep(0.1)


def write_to_file(message_list):
    r = open('stuf/all_messages.txt', 'w', encoding='utf8')
    for i in range(len(message_list)):
        r.write(message_list[i])
        if i + 1 != len(message_list):
            r.write('\n')
    r.close()


def message_count(flag, saved_number):
    a, b = 99, 100
    c = 0
    i = 0
    while True:
        try:
            pg.press('home')
            time.sleep(0.1)
            pg.scroll(7)
            pg.scroll(-2)
            if i % 5 == 0:
                a, b = b, req_url(driver.page_source, flag=flag, saved_number=saved_number)
                print()
                if a == b:
                    print(a)
                    c += 1
                else:
                    c = 0
                if c == 5:
                    a = b = 0
                    break
            print(end='.')
            i += 1
        except:
            print(i)

    write_to_file(req_url(driver.page_source, key=1, flag=flag, saved_number=saved_number))
    return req_url(driver.page_source, flag=flag, saved_number=saved_number)


def sorted_text_list():
    r = open('stuf/all_messages.txt', 'r', encoding='utf8')
    txt_list = np.array([])
    for i in r:
        try:
            txt_list = np.append(txt_list, str(''.join(i.splitlines())).replace('1×', ''))
        except:
            print('exc136: ', str(''.join(i.splitlines())))
    if 'Сообщения защищены сквозным шифрованием.' in txt_list[0]:
        txt_list = np.delete(txt_list, 0)
    return txt_list
