import time

import pyautogui as pg
from selenium import webdriver
from selenium.webdriver.common.by import By

from bs4_code import req_url
from config import contact, archive, select_ico, message_class_list


def print_time(tic, toc, text='?'):
    print("used time for {}: {} sec".format(text, (tic - toc)))
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


tic = time.time()
options = webdriver.ChromeOptions()
options.add_argument(r'--user-data-dir=C:\Users\OFFICE\AppData\Local\Google\Chrome\User Data\Default')
options.add_argument('--profile-directory=Default')

driver = webdriver.Chrome(executable_path=r'C:\Users\OFFICE\PycharmProjects\whatsapp-project\chromedriver.exe',
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

messages = driver.find_element(By.XPATH, '//div[@class="{}"]'.format("n5hs2j7m oq31bsqd lqec2n0o eu5j4lnj")). \
        find_elements(By.XPATH, '//div[@data-id]')
sorted_messages = []
print('len messages: ', len(messages))

for mes in messages:
    # print(mes.get_attribute('innerHTML'))
    if 'visual-checkbox' in mes.get_attribute('innerHTML'):
        # print('*', end='')
        sorted_messages.append(mes)
print('len sorted_m: ', len(sorted_messages))

toc = time.time()
tic = print_time(tic, toc, "array1")

# print(len(messages))
# print(len(messages))
# select
r = open('text.txt', 'r', encoding='utf8')
for i in r:
    print('+')
    for j in sorted_messages:
        print('.', end='')
        temp_line = j.text.splitlines()
        n = ''.join(temp_line)
        if str(n) == str(i.splitlines()[0]):
            print("success")
            # problem here. need to choose next element if this was selected
            selected = j.find_element(By.XPATH, '//div[@class="{}"]'.format(
                select_ico))
            selected.click()
            break


toc = time.time()
tic = print_time(tic, toc, "array2")
            # pg.keyDown()
#
#     select('//div[@class="{}"]', select_message_class, 1, True)

# bs4_code.select_all_text(driver.page_source, message_class)
# bs4_code.select_photo_scr(driver.page_source, photo_class)
# sum_div = bs4_code.req_url(driver.page_source)
input()
driver.quit()
