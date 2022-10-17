import time

import pyautogui as pg
from selenium import webdriver
from selenium.webdriver.common.by import By

from bs4_code import req_url
from config import contact, archive, message_class, select_message_class


def select(xpath, class_name, text='NULL', click=0):
    selected = driver.find_element(By.XPATH, xpath.format(class_name))
    if click == 1:
        selected.click()
    if text != 'NULL':
        print(text)
    # if ms:
    #     return 1
    time.sleep(0.5)


options = webdriver.ChromeOptions()
options.add_argument(r'--user-data-dir=C:\Users\OFFICE\AppData\Local\Google\Chrome\User Data\Default')
options.add_argument('--profile-directory=Default')

driver = webdriver.Chrome(executable_path=r'C:\Users\OFFICE\PycharmProjects\whatsapp-project\chromedriver.exe',
                          options=options)
driver.get("https://web.whatsapp.com")

while True:  # waiting for wa
    try:
        select('//button[@class="{}"]', archive, "archive opened", click=1)
        break
    except:
        print("not yet")
        time.sleep(1)
select('//span[@title="{}"]', contact, "contact opened", 1)
select('//span[@class="{}"]', message_class)
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

s, message_list = req_url(driver.page_source, 1)
# i = 0
# while i <= s:
#
#     select('//div[@class="{}"]', select_message_class, 1, True)

# bs4_code.select_all_text(driver.page_source, message_class)
# bs4_code.select_photo_scr(driver.page_source, photo_class)
# sum_div = bs4_code.req_url(driver.page_source)
input()
driver.quit()
