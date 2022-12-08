import os
import sys
import time
import pyautogui as pg
from bs4_code import req_url


# noinspection PyGlobalUndefined
def set_driver_by(d, B):
    global driver
    global By
    driver, By = d, B


def click(click_c=1):
    for i in range(click_c):
        pg.click(389, 777, button='middle')


def delete_text_from_str(tt):
    tt = tt.replace('Пересланное сообщение', '')
    return tt


def split_text_date(td, r):
    # print(td)
    ti = td.index(':')
    date = td[ti - 2:ti + 3]
    text = td[:ti - 2]
    if '**' in text:
        temp_text = text.split('**')[1]
    else:
        temp_text = text
    if 'Пересланное сообщение' in temp_text:
        temp_text = delete_text_from_str(temp_text)
    if temp_text not in ['', ' ']:
        r.write(date + '-' + temp_text+'\n')


def taking_sorted_messages(saved_number=0):
    try:
        tsm_time = time.time()
        messages = driver.find_element(
            By.XPATH, '//div[@class="{}"]'.format("n5hs2j7m oq31bsqd lqec2n0o eu5j4lnj")). \
            find_elements(By.XPATH, '//div[@data-id]')
        sm, smt = [], []
        r = open('stuf/sorted_messages_list.txt', 'w', encoding='utf8')
        if saved_number != 0:
            for mes in messages:
                text_date = str(''.join(''.join(mes.text.splitlines())))
                mes_html = mes.get_attribute('innerHTML')
                if '_1-lf9 _3mSPV' not in mes_html:
                    if '_1-lf9 _25eIs' not in mes_html:
                        # if any(a not in mes.get_attribute('innerHTML') for a in ['_1-lf9 _3mSPV', '_1-lf9 _25eIs']):
                        sm.append(mes)
                        smt.append(text_date)
                        if '**' in text_date:
                            temp = text_date.split('**')
                            if len(temp[1].split(':')[0]) > 2:
                                try:
                                    split_text_date(text_date, r)
                                except:
                                    print('f63: {}'.format(text_date))
                else:
                    try:
                        split_text_date(text_date, r)
                    except:
                        print('f68: {}'.format(text_date))
            # надо сохранить еще сообщения
            print("saved, number = {}, time = ".format(saved_number), time.time()-tsm_time)
            temp_text = open('stuf/temp_text.txt', 'w', encoding='utf8')
            for s in sm:
                temp_text.write(s.text)
            return sm, smt
        else:
            for mes in messages:
                text_date = str(''.join(''.join(mes.text.splitlines())))
                smt.append(text_date)
            print("saved, number = {}, time = ".format(saved_number), time.time()-tsm_time)
            return messages, smt
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print('f84: ', exc_type, fname, exc_tb.tb_lineno, e)


def select(xpath, class_name, text='NULL', clicked=0):
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
    mes_cunt, message_div_sum, message_div_sum2 = 0, 99, 100
    result_repeated = 0
    while result_repeated < 7:
        pg.press('home')
        print("{}...".format(mes_cunt), end='')
        time.sleep(0.5)
        if mes_cunt % 5 == 0:
            pg.scroll(7)
            pg.scroll(-2)
            message_div_sum2, message_div_sum = message_div_sum, req_url(driver.page_source, flag=flag,
                                                                         saved_number=saved_number)
            print('found mes sum: ', message_div_sum)
        if message_div_sum == message_div_sum2:
            result_repeated += 1
        else:
            result_repeated = 0
        mes_cunt += 1
    a = time.time()
    write_to_file(req_url(driver.page_source, key=1, flag=flag, saved_number=saved_number))
    print(time.time()-a)
    return message_div_sum


def sorted_text_list():
    r = open('stuf/all_messages.txt', 'r', encoding='utf8')
    txt_list = []
    for i in r:
        try:
            txt_list.append(str(''.join(i.splitlines())))
        except:
            print('exc136: ', str(''.join(i.splitlines())))
    return txt_list
