import time

import pyautogui as pg
from selenium import webdriver
from selenium.webdriver.common.by import By

from bs4_code import req_url
from config import contact, archive, select_ico, not_selected_ico_class


def print_time(ttic, ttoc, text='?'):
    print("used time for {}: {} sec".format(text, (ttic - ttoc)))
    return time.time()


def select(xpath, class_name, text='NULL', click=0, ms=False):
    selected_element = driver.find_element(By.XPATH, xpath.format(class_name))
    if click == 1:
        selected_element.click()
    if text != 'NULL':
        print(text)
    time.sleep(0.5)

    if ms:
        return 1
    else:
        return 0


def taking_sorted_messages(solo=0, check=False):
    messages = driver.find_element(
        By.XPATH, '//div[@class="{}"]'.format("n5hs2j7m oq31bsqd lqec2n0o eu5j4lnj")). \
        find_elements(By.XPATH, '//div[@data-id]')
    sm = []
    # print('len messages: ', len(messages))
    for mes in messages:
        # print(mes.get_attribute('innerHTML'))
        if 'visual-checkbox' in mes.get_attribute('innerHTML'):
            sm.append(mes)

    if check==True:
        return sm[solo]
    else:
        return sm


tic = time.time()
options = webdriver.ChromeOptions()
options.add_argument(r'--user-data-dir=C:\Users\OFFICE\AppData\Local\Google\Chrome\User Data\Default')
options.add_argument('--profile-directory=Default')

driver = webdriver.Chrome\
    (executable_path=r'C:\Users\OFFICE\PycharmProjects\whatsapp-project\chromedriver.exe',
                          options=options)
driver.get("https://web.whatsapp.com")

while True:  # waiting for wa
    try:
        # выбор архива
        select('//button[@class="{}"]', archive, "archive opened", click=1)
        break
    except:
        time.sleep(1)
toc = time.time()
tic = print_time(tic, toc, "begin")
# выбор контакта
select('//span[@title="{}"]', contact, "contact opened", 1)
# select('//span[@class="{}"]', message_class, ms=True)
pg.click(913, 617)
i = 0
a, b = 0, 1
while True:
    pg.press('home')
    print("{}...".format(i), end='')
    time.sleep(0.3)
    if i % 5 == 0:
        b, a = a, req_url(driver.page_source)
        if a == b:
            break
    i += 1

toc = time.time()
tic = print_time(tic, toc, "step2")

s, message_list = req_url(driver.page_source, 1)

r = open('text.txt', 'w', encoding='utf8')
for i in message_list:
    r.write(i)
    if i != message_list[len(message_list) - 1]:
        r.write('\n')
r.close()

select('//div[@class="{}"]', '_28_W0', click=1)  # click menu
select('//div[@aria-label="{}"]', 'Выбрать сообщения', click=1)

toc = time.time()
tic = print_time(tic, toc, "selects")

sorted_messages = taking_sorted_messages()

print('len sorted_m: ', len(sorted_messages))

toc = time.time()
tic = print_time(tic, toc, "array1")

r = open('text.txt', 'r', encoding='utf8')
# l = 0
n=''
for i in r:
    for j in range(len(sorted_messages)):
        temp_line = sorted_messages[j].text.splitlines()
        n1=n
        n = ''.join(temp_line)

        print(sorted_messages[j].get_attribute('innerHTML'))
        if (str(n) == str(i.splitlines()[0]))&(n1!=n):
            if 'img' in sorted_messages[j].get_attribute('innerHTML'):
                if '_3BK98' in str(sorted_messages[j].get_attribute('innerHTML')):
                    if "_3BK98 _3vy-1" not in str(sorted_messages[j].get_attribute('innerHTML')):
                        print(i.splitlines()[0], ' - ', n)
                        print('+', sorted_messages[j].get_attribute('innerHTML'))
                        selected = sorted_messages[j].find_element(By.XPATH, '//div[@class="{}"]'.
                                                                   format(select_ico))
                        selected.click()
                        sorted_messages[j] = taking_sorted_messages(j, True)
                        break
                    else:
                        print("-")

        # temp_line = j.text.splitlines()
        # n = ''.join(temp_line)
        #
        # # if l < 3:
        # #     print("i: ", str(i.splitlines()[0]) , "\nn: ", n)
        # #     print("1: ", j.get_attribute('innerHTML'))
        # #     print("2: ", j.get_attribute('class'))
        # # print("2: ", j.find_element(By.XPATH, '//div[@class="{}"]'.format(select_ico)))
        #
        # # problem here. need to choose next element if this was selected
        # if str(n) == str(i.splitlines()[0]):
        #     l += 1
        #     print(l)
        #     print(j.get_attribute('class'))
        #     if "_3Zpy8" not in str(j.get_attribute('class')):
        #
        #         selected = j.find_element(By.XPATH, '//div[@class="{}"]'.format(select_ico))
        #         selected.click()
        #
        #         sorted_messages.remove(j)
        #
        #         print("after remove: ", len(sorted_messages))
        #         print("+: ", j.get_attribute('innerHTML'))
        #         # pg.press('down')
        #         break

toc = time.time()
tic = print_time(tic, toc, "array2")

# bs4_code.select_all_text(driver.page_source, message_class)
# bs4_code.select_photo_scr(driver.page_source, photo_class)
# sum_div = bs4_code.req_url(driver.page_source)
input()
driver.quit()
