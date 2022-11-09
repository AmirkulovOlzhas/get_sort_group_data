import time
import pyautogui as pg
from bs4_code import req_url


def set_driver_by(d, B):
    global driver
    global By
    driver, By = d, B


def click(click_c=1):
    for i in range(click_c):
        pg.click(913, 617, button='middle')


def split_text_date(td):
    date = td[-5:]
    text = td[:-5]
    print(date, ' - ', text.split('**')[1] if '**' in text else text)


def taking_sorted_messages(saved_number=0):
    messages = driver.find_element(
        By.XPATH, '//div[@class="{}"]'.format("n5hs2j7m oq31bsqd lqec2n0o eu5j4lnj")). \
        find_elements(By.XPATH, '//div[@data-id]')
    sm = []
    if saved_number != 0:
        for mes in messages:
            text_date = str(''.join(''.join(mes.text.splitlines())))
            if '_1-lf9 _3mSPV' not in mes.get_attribute('innerHTML'):
                sm.append(mes)
                if '**' in text_date:
                    temp = text_date.split('**')
                    if len(temp[1].split(':')[0]) > 2:
                        print('+', end='')
                        split_text_date(text_date)
            else:
                print('-', end='')
                split_text_date(text_date)
        # надо сохранить еще сообщения
        return sm
    else:
        return messages


def select(xpath, class_name, text='NULL', clicked=0):
    selected_element = driver.find_element(By.XPATH, xpath.format(class_name))
    if clicked == 1:
        selected_element.click()
    if text != 'NULL':
        print(text)
    time.sleep(0.1)


def write_to_file(message_list):
    r = open('stuf/text.txt', 'w', encoding='utf8')
    for i in range(len(message_list)):
        r.write(message_list[i])
        if i + 1 != len(message_list):
            r.write('\n')
    r.close()


def message_count(flag, saved_number):
    mes_cunt, message_div_sum, message_div_sum2 = 0, 99, 100
    message_div_sum2, message_div_sum = message_div_sum, req_url(driver.page_source, flag=flag,
                                                                 saved_number=saved_number)
    pg.press('home')
    result_repeated = 0
    while True:
        pg.press('home')
        print("{}...".format(mes_cunt), end='')
        if mes_cunt % 5 == 0:
            pg.scroll(7)
            pg.scroll(-2)
            time.sleep(0.3)
            message_div_sum2, message_div_sum = message_div_sum, req_url(driver.page_source, flag=flag,
                                                                         saved_number=saved_number)
            if message_div_sum == message_div_sum2:
                result_repeated += 1
            else:
                result_repeated = 0
            if result_repeated > 5:
                break
        mes_cunt += 1
    write_to_file(req_url(driver.page_source, key=1, flag=flag, saved_number=saved_number))
    return message_div_sum


def sorted_text_list():
    r = open('stuf/text.txt', 'r', encoding='utf8')
    txt_list = []
    click(2)
    for i in r:
        txt_list.append(str(''.join(i.splitlines())))
    return txt_list
