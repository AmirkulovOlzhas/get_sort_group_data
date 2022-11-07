import time
import pyautogui as pg
from lxml import etree, html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fucions import taking_sorted_messages, select, write_to_file, click
from bs4_code import req_url
from test import start_park_rename
from config import contact, archive, select_ico, argument1, argument2, msg_cont_class

while True:
    flag = int(input("park-0, enb-1, abai-2: "))
    saved_number = int(input("0 - not saved numbers mes, 1 saved: "))
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
        select(driver, By, '//button[@class="{}"]', archive, "archive opened", clicked=1)
        break
    except:
        time.sleep(1)

# выбор контакта
select(driver, By, '//span[@title="{}"]', contact[int(flag)], "contact opened", 1)
time.sleep(2)
click(pg)
# try: #!!!
#     pg.scroll(-5)
#     select(driver, By, '//span[@class="{}"]', '_3K42l', clicked=1)
#     print('1s')
#     time.sleep(2)
#     select(driver, By, '//div[@class="{}"]', '_1GLVO _165_h', click=1)
#     print('2s')
#     time.sleep(2)
#     select(driver, By, '//div[@class="{}"]', '_27Uai', click=1)
#     print('3s')
#     # time.sleep(2)
#     # pg.scroll(-5)
#     print('pg down')
#     # time.sleep(2)
# except Exception as e:
#     print('not pg down - ', e)
mes_cunt, message_div_sum, message_div_sum2 = 0, 99, 100
message_div_sum2, message_div_sum = message_div_sum, req_url(driver.page_source, flag=flag, saved_number=saved_number)

pg.press('home')
result_repeated=0
while True:
    pg.press('home')
    print("{}...".format(mes_cunt), end='')
    if mes_cunt % 5 == 0:
        pg.scroll(7)
        pg.scroll(-2)
        time.sleep(0.3)
        message_div_sum2, message_div_sum = message_div_sum, req_url(driver.page_source, flag=flag, saved_number=saved_number)
        if message_div_sum == message_div_sum2:
            result_repeated+=1
        else:
            result_repeated=0
        if result_repeated>5:
            break
    mes_cunt += 1

write_to_file(req_url(driver.page_source, key=1, flag=flag, saved_number=saved_number))

select(driver, By, '//div[@class="{}"]', '_28_W0', clicked=1)  # click menu
select(driver, By, '//div[@aria-label="{}"]', 'Выбрать сообщения', clicked=1)

sorted_messages = taking_sorted_messages(driver, By, saved_number = int(saved_number))
print('len sorted_m: ', len(sorted_messages))

r = open('text.txt', 'r', encoding='utf8')
sum, txt_list = 0, []
click(pg, 2)

for i in r:
    txt_list.append(str(''.join(i.splitlines())))
time_a = time.time()
for mes in sorted_messages:
        j_text = str(''.join(''.join(mes.text.splitlines())))
        print(j_text)
        if j_text in txt_list:
            try:
                driver.execute_script("arguments[0].click();",
                                      mes.find_element(By.CLASS_NAME, select_ico))
            except Exception as e:
                print(f"exception handled - {e}")
                wait = WebDriverWait(driver, 10)
                element= wait.until(EC.element_to_be_clickable(By.CLASS_NAME.format(select_ico)))
            txt_list.remove(j_text)
            sum += 1

print(len(txt_list))
print(time.time() - time_a)
print("sum = {}".format(sum))

if flag == 0:
    start_park_rename()
# bs4_code.select_all_text(driver.page_source, message_class)
# bs4_code.select_photo_scr(driver.page_source, photo_class)
# sum_div = bs4_code.req_url(driver.page_source)
if input("Download? 1-yes everything else - no: ") == '1':
    select(driver, By, '//span[@data-testid="{}"]', class_name='download', clicked=1)
else:
    print('okay')

input()
driver.quit()