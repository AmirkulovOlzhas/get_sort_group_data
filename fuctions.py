import os
import re
import sys
import time

import numpy as np
import pyautogui as pg
from config import chat, not_select_messages, contacts, not_saved_contact


# noinspection PyGlobalUndefined
def set_driver_by(d, B):
    global driver
    global By
    driver, By = d, B


def click(click_c=1):
    for i in range(click_c):
        pg.click(389, 777, button='middle')


def split_text_date(contact_name, td):
    try:
        abc = '1234567890:+ Видео'
        text = ''
        date = re.findall(f'\d\d\:\d\d', ''.join(td))[-1]
        for word in td:
            if not all(letter in abc for letter in word):
                if word not in ['Пересланное сообщение', 'Данное сообщение удалено']:
                    if '**' not in word:
                        if word not in not_saved_contact:
                            text += word
                        else:
                            contact_name += '|' + word
        if text:
            s = date + '|' + contact_name + ' - ' + text + '\n'
            return s
    except:
        pass


def get_contact_info(m, contact):
    contact_number = None
    try:
        contact_number = re.findall(r'\_77\d{9}', m.get_attribute("data-id"))[-1][1:]
        contact_name = contacts[contact][contact_number]
    except:
        contact_name = None
    return contact_name, contact_number


def mess_count():
    return len(driver.find_element(
        By.XPATH, '//div[@class="{}"]'.format(chat)). \
               find_elements(By.XPATH, '//div[@data-id]'))


def taking_sorted_messages(saved_number=0, contact=0):
    try:
        start_time = time.time()
        messages = np.array(driver.find_element(
            By.XPATH, '//div[@class="{}"]'.format(chat)). \
                            find_elements(By.XPATH, '//div[@data-id]'))
        sm, smt, text_arr = np.array([]), [], np.array([])
        if saved_number in [1, 3]:
            # time_1 = '24:00'
            messages_classes = np.array(driver.find_element(
                By.XPATH, '//div[@class="{}"]'.format(chat)). \
                                        find_elements(By.XPATH, '//div[@data-id]//div[contains(@class, "_1-lf9")]'))
        if saved_number == 1:
            ab_func = lambda x: [x[1], x[0]]
        else:
            ab_func = lambda x: x

        for i in range(len(messages)):
            print(end='.')
            if i % 7 == 0:
                print()
            x = 0
            contact_name, contact_number = get_contact_info(messages[i], contact)
            a, b = ab_func([contact_number, contact_name])
            # saved_number: 0 - select all messages from not saved numbers
            # 1 - select only photos only from saved contacts
            # 2 - select all, from all
            # 3 - select only photo only
            if a:
                if saved_number == 2:
                    x = 1
                elif saved_number == 0:
                    if b is None:
                        x = 1
                else:
                    mes_class = np.array(messages_classes[i].get_attribute("class").split())
                    if all(bad_class not in mes_class for bad_class in not_select_messages):
                        x = 1
                    if contact_name is None:
                        contact_name = contact_number
                if x == 1:
                    sm = np.append(sm, messages[i])
                    smt.append(messages[i].text.splitlines())  # text_date
                if saved_number in [1, 3]:
                    text_arr = np.append(text_arr, split_text_date(contact_name, messages[i].text.splitlines()))

        print('\n-------------------------------\ntime for tsm: ', time.time() - start_time,
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


def message_count():
    a, b = 99, 100
    c, i = 0, 0
    error_count = 0
    while error_count < 5:
        try:
            pg.press('home')
            time.sleep(0.1)
            pg.scroll(7)
            pg.scroll(-2)
            if i % 5 == 0:
                a, b = b, mess_count()
                print()
                if a == b:
                    print(a)
                    c += 1
                else:
                    c = 0
                if c == 3:
                    break
            print(end='.')
            i += 1

        except:
            time.sleep(1)
            print(f'Ошибка {5 - error_count}')
            error_count += 1
    if error_count == 7:
        return 0
    return mess_count()
