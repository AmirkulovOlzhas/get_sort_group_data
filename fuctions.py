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
        a = time.time()
        messages = np.array(driver.find_element(
            By.XPATH, '//div[@class="{}"]'.format(chat)). \
                            find_elements(By.XPATH, '//div[@data-id]'))
        sm, smt, text_arr = np.array([]), [], np.array([])

        if saved_number == 1:
            messages_classes = np.array(driver.find_element(
                By.XPATH, '//div[@class="{}"]'.format(chat)). \
                                        find_elements(By.XPATH, '//div[@data-id]//div[contains(@class, "_1-lf9")]'))
            for i in range(len(messages)):
                mes_class = np.array(messages_classes[i].get_attribute("class").split())
                contact_name, contact_number = get_contact_info(messages[i], contact)

                if contact_name:  # not_select_mess
                    m = messages[i].text.splitlines()
                    if all(bad_class not in mes_class for bad_class in not_select_messages):
                        sm = np.append(sm, messages[i])
                        smt.append(m)  # text_date
                    text_arr = np.append(text_arr, split_text_date(contact_name, m))

        elif saved_number == 0:
            for mes in messages:
                m, k = mes.text.splitlines(), 0
                contact_name, contact_number = get_contact_info(mes, contact)
                if contact_number:
                    if contact != 4:
                        if contact_name is None:
                            k = 1
                    else:
                        if contact_number in ['77474490473', '77475421701', '77053655758',
                                              '77085482053', '77765870727', '77028948707']:
                            k = 1
                if k == 1:
                    smt.append(m)
                    sm = np.append(sm, mes)

        elif saved_number == 3:  # choose all photos
            messages_classes = np.array(driver.find_element(
                By.XPATH, '//div[@class="{}"]'.format(chat)). \
                                        find_elements(By.XPATH, '//div[@data-id]//div[contains(@class, "_1-lf9")]'))

            for i in range(len(messages)):
                contact_name, contact_number = get_contact_info(messages[i], contact)
                m = messages[i].text.splitlines()
                mes_class = np.array(messages_classes[i].get_attribute("class").split())
                if contact_number:
                    if all(bad_class not in mes_class for bad_class in not_select_messages):
                        smt.append(m)
                        sm = np.append(sm, messages[i])
                    if contact_name is None:
                        contact_name = contact_number
                    text_arr = np.append(text_arr, split_text_date(contact_name, m))
        else:  # choose all (text too)
            for mes in messages:
                m = mes.text.splitlines()
                contact_name, contact_number = get_contact_info(mes, contact)
                if contact_number:
                    smt.append(m)
                    sm = np.append(sm, mes)


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


def message_count():
    a, b = 99, 100
    c, i = 0, 0
    while True:
        try:
            pg.press('home')
            time.sleep(0.1)
            pg.scroll(7)
            pg.scroll(-2)
            #if mes[0].text[n] != 'Сообщение'
            if i % 5 == 0:
                a, b = b, mess_count()
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
    return mess_count()
