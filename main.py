import time

import pyautogui as pg
from selenium import webdriver
from selenium.webdriver.common.by import By

import bs4_code
from config import contact, archive, message_class, photo_class


def select(xpath, class_name, text='NULL', click=0):
    selected = driver.find_element(By.XPATH, xpath.format(class_name))
    if click == 1:
        selected.click()
    if text != 'NULL':
        print(text)
    time.sleep(2)


options = webdriver.ChromeOptions()
options.add_argument(r'--user-data-dir=C:\Users\OFFICE\AppData\Local\Google\Chrome\User Data\Default')
options.add_argument('--profile-directory=Default')

driver = webdriver.Chrome(executable_path=r'C:\Users\OFFICE\PycharmProjects\whatsapp-project\chromedriver.exe',
                          options=options)
driver.get("https://web.whatsapp.com")

i = 15
while i > 0:
    print("Waiting...{}".format(i))
    time.sleep(1)
    i -= 1
print("Logged In")
time.sleep(2)

select('//button[@class="{}"]', archive, "archive opened", click=1)
select('//span[@title="{}"]', contact, "contact opened", 1)
select('//span[@class="{}"]', message_class)
pg.click(913, 617)
for i in range(10):
    pg.press('home')
    print("home pressed")
    time.sleep(1)

bs4_code.select_all_text(driver.page_source, message_class)
bs4_code.select_photo_scr(driver.page_source, photo_class)
time.sleep(20)
driver.quit()
