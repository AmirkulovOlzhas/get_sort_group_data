import time
import pyautogui as pg
from lxml import etree, html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fucions import taking_sorted_messages, select, write_to_file, click
from bs4_code import req_url
from config import contact, archive, select_ico, argument1, argument2, msg_cont_class

while True:
    flag = input("park-0, enb-1, abai-2: ")
    saved_number = input("0 - not saved numbers mes, 1 saved: ")
    if int(flag) in [0,1,2] and int(saved_number) in [0,1]:
        print("Selected {}".format(flag))
        break
    else:
        print('set one of 012')

options = webdriver.ChromeOptions(); options.add_argument(argument1); options.add_argument(argument2)

driver = webdriver.Chrome\
    (executable_path=r'C:\Users\OFFICE\PycharmProjects\whatsapp-project\chromedriver.exe',
                          options=options)
driver.get("https://web.whatsapp.com")

while True:  # waiting for wa
    try:
        # выбор архива
        select(driver, By, '//button[@class="{}"]', archive, "archive opened", click=1)
        break
    except:
        time.sleep(1)

# выбор контакта
select(driver, By, '//span[@title="{}"]', contact[int(flag)], "contact opened", 1)
time.sleep(2)
click(pg)
try:
    select(driver, By, '//div[@class="{}"]', '_27Uai', click=1)
    print('pg down')
    time.sleep(2)
except Exception as e:
    print('not pg down - ', e)
mes_cunt, message_div_sum, message_div_sum2 = 0, 99, 100
message_div_sum2, message_div_sum = message_div_sum, req_url(driver.page_source, flag=flag, saved_number=saved_number)

pg.press('home')
while True:
    pg.press('home')
    print("{}...".format(mes_cunt), end='')
    time.sleep(0.3)
    if mes_cunt % 7 == 0:
        pg.scroll(7)
        pg.scroll(-2)
        message_div_sum2, message_div_sum = message_div_sum, req_url(driver.page_source, flag=flag, saved_number=saved_number)
        if message_div_sum == message_div_sum2:
            if mes_cunt > 15:
                print("break")
                break
    mes_cunt += 1

write_to_file(req_url(driver.page_source, key=1, flag=flag, saved_number=saved_number))

select(driver, By, '//div[@class="{}"]', '_28_W0', click=1)  # click menu
select(driver, By, '//div[@aria-label="{}"]', 'Выбрать сообщения', click=1)

sorted_messages, sum = taking_sorted_messages(driver, By, saved_number = saved_number)
print('len sorted_m: ', len(sorted_messages), ' - ', sum)

r = open('text.txt', 'r', encoding='utf8')
j_text, sum= '', 0
click(pg, 2)

for i in r:
    i_text = str(''.join(i.splitlines()))
    time_a = time.time()
    for j in range(len(sorted_messages)):
        if sorted_messages[j]:
            j_text, j_html = str(''.join(''.join(sorted_messages[j].text.splitlines()))), str(sorted_messages[j].get_attribute('innerHTML'))
            if i_text==j_text:
                try:
                    driver.execute_script("arguments[0].click();",
                                          sorted_messages[j].find_element(By.CLASS_NAME, select_ico))
                except Exception as e:
                    print(f"exception handled - {e}")
                    wait = WebDriverWait(driver, 10)
                    element= wait.until(EC.element_to_be_clickable(By.CLASS_NAME.format(select_ico)))
                # sorted_messages[j] = 'none'
                sorted_messages.remove(sorted_messages[j])
                sum += 1
                break

    print(time.time() - time_a)

print("sum = {}".format(sum))

# bs4_code.select_all_text(driver.page_source, message_class)
# bs4_code.select_photo_scr(driver.page_source, photo_class)
# sum_div = bs4_code.req_url(driver.page_source)
if input("Download? 1-yes everything else - no: ") == 'yes':
    select(driver, By, '//span[@data-testid="{}"]', class_name='download', click=1)
else:
    print('okay')

input()
driver.quit()