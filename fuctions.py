import os
import re
import sys
import time

import numpy as np
import pyautogui as pg
from bs4_code import req_url, count_mes_in_chat
from config import chat, not_select_messages, contact_place


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
    try:
        a = time.time()
        messages = np.array(driver.find_element(
            By.XPATH, '//div[@class="{}"]'.format(chat)). \
                            find_elements(By.XPATH, '//div[@data-id]'))
        sm, smt, text_arr = np.array([]), [], np.array([])
        if saved_number:
            messages_classes = np.array(driver.find_element(
                By.XPATH, '//div[@class="{}"]'.format(chat)). \
                                        find_elements(By.XPATH, '//div[@data-id]//div[contains(@class, "_1-lf9")]'))
            for i in range(len(messages)):
                m = messages[i].text.splitlines()
                text_date = ''.join(m)  # print('-', '---'.join(m))
                mes_class = np.array(messages_classes[i].get_attribute("class").split())
                # print(re.findall(r'\_\d{11}\@', messages[i].get_attribute("data-testid"))[0][1:-1])
                if '+7 7' not in text_date:  # not_select_mess
                    if all(bad_class not in mes_class for bad_class in not_select_messages):
                        sm = np.append(sm, messages[i])
                        smt.append(m)  # text_date
                    if len(text_date.split(':')[0]) > 2:
                        text_arr = np.append(text_arr, split_text_date(text_date))

        else:
            for mes in messages:
                m, k = mes.text.splitlines(), 0
                if len(m) > 1:
                    temp_value = None
                    if contact in [1, 2]:
                        temp_value = contact_place[contact]
                    if contact != 4:
                        if temp_value:
                            if ''.join(m)[0:4] != temp_value:  # print('-', '---'.join(mes.text.splitlines()))
                                k = 1
                        else:
                            k = 1
                    else:
                        text_date = ''.join(m)
                        if any(number in text_date for number in
                               ['+7 747 449 0473', '+7 747 542 1701', '+7 705 365 5758',
                                '+7 708 548 2053', '+7 776 587 0727', '+7 702 894 8707']):
                            k = 1
                    if k == 1:
                        smt.append(m)
                        sm = np.append(sm, mes)

        if 'Сообщения защищены' in smt[0][0]:
            sm = np.delete(sm, 0)
            smt.remove(smt[0])
        messages = None
        print('\n-------------------------------\ntime for tsm: ', time.time() - a,
              '\n-----------------------------------')
        return sm, smt, text_arr
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno, e)


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
    c, i = 0, 0
    page = None
    while True:
        try:
            pg.press('home')
            time.sleep(0.1)
            pg.scroll(7)
            pg.scroll(-2)
            page = driver.page_source
            if i % 5 == 0:
                a, b = b, count_mes_in_chat(page)
                print()
                if a == b:
                    print(a)
                    c += 1
                else:
                    c = 0
                if c == 4:
                    break
            print(end='.')
            i += 1

        except:
            print(i)
    write_to_file(req_url(page, flag=flag, saved_number=saved_number))
    return count_mes_in_chat(page)


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
