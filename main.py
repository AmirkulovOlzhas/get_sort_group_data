import time
import pyautogui as pg
from lxml import etree, html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fucions import taking_sorted_messages, select, write_to_file, click
from bs4_code import req_url
from config import contact, archive, select_ico, argument1, argument2,\
    select_ico2,select_ico3,select_ico_input,select_ico4, msg_cont_class

while True:
    flag = input("park-0, enb-1, abai-2: ")
    if int(flag) in [0,1,2]:
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
click(pg)

mes_cunt, message_div_sum, message_div_sum2 = 0, 0, 1
message_div_sum2, message_div_sum = message_div_sum, req_url(driver.page_source)
while True:
    pg.press('home')
    print("{}...".format(mes_cunt), end='')
    time.sleep(0.3)
    if mes_cunt % 5 == 0:
        message_div_sum2, message_div_sum = message_div_sum, req_url(driver.page_source)
        if message_div_sum == message_div_sum2:
            break1
    mes_cunt += 1

write_to_file(req_url(driver.page_source, key=1))

select(driver, By, '//div[@class="{}"]', '_28_W0', click=1)  # click menu
select(driver, By, '//div[@aria-label="{}"]', 'Выбрать сообщения', click=1)

sorted_messages, sum = taking_sorted_messages(driver, By)
print('len sorted_m: ', len(sorted_messages), ' - ', sum)

r = open('text.txt', 'r', encoding='utf8')
j_text, sum= '', 0
click(pg, 2)
for i in r:
    i_text = str(''.join(i.splitlines()))
    for j in range(len(sorted_messages)):
        if(sorted_messages[j])!='none':
            temp_line = sorted_messages[j].text.splitlines()
            j_text = str(''.join(''.join(temp_line)))
            j_html = str(sorted_messages[j].get_attribute('innerHTML'))
            print(i_text,' - ', j_text, '\n', type(i_text), ' - ', type(j_text))
            if i_text==j_text:
                try:
                    # document_root = html.document_fromstring(j_html)
                    # print(etree.tostring(document_root, encoding='unicode', pretty_print=True))
                    selected = sorted_messages[j].find_element(By.XPATH, '//div[@data-testid="{}"]'.
                                                               format('msg-container'))
                    selected1 = sorted_messages[j].find_element(By.XPATH, '//div[@class="{}"]'.
                                                               format('_3BK98'))
                    print("-", str(selected.get_attribute('class')))

                    try:
                        driver.execute_script("arguments[0].click();",
                                              sorted_messages[j].find_element(By.CLASS_NAME, '_3BK98'))
                    except Exception as e:
                        print(f"exception handled - {e}")
                        wait = WebDriverWait(driver, 10)
                        element= wait.until(EC.element_to_be_clickable(By.CLASS_NAME.format('_3BK98')))
                    sorted_messages[j] = 'none'
                    sum += 1
                    time.sleep(0.1)
                    break

                except Exception as e:
                    print("-----------------------\nwrong: {}".format(e))
                    print(j_html)
                finally:
                    print(j_text, ' - ', i_text, '\n--------------------')


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