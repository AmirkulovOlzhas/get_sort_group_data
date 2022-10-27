import time

import pyautogui as pg
from lxml import etree, html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fucions import taking_sorted_messages, select, write_to_file
from bs4_code import req_url
from config import contact, archive, select_ico, argument1, argument2,\
    select_ico2,select_ico3,select_ico_input,select_ico4, msg_cont_class


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
select(driver, By, '//span[@title="{}"]', contact, "contact opened", 1)

pg.click(913, 617, button='middle')

i = 0
message_div_sum, message_div_sum2 = 0, 1
while True:
    pg.press('home')
    print("{}...".format(i), end='')
    time.sleep(0.3)
    if i % 5 == 0:
        message_div_sum2, message_div_sum = message_div_sum, req_url(driver.page_source)
        if message_div_sum == message_div_sum2:
            break
    i += 1

message_list = req_url(driver.page_source, key=1)
write_to_file(message_list)

select(driver, By, '//div[@class="{}"]', '_28_W0', click=1)  # click menu
select(driver, By, '//div[@aria-label="{}"]', 'Выбрать сообщения', click=1)

sorted_messages, sum = taking_sorted_messages(driver, By)
print('len sorted_m: ', len(sorted_messages), ' - ', sum)

r = open('text.txt', 'r', encoding='utf8')
j_text= ''
sum = 0
list_sum=0
pg.click(913, 617, button='middle')
for i in r:
    i_text = str(''.join(i.splitlines()))
    for j in range(len(sorted_messages)):
        if(sorted_messages[j])!='none':
            temp_line = sorted_messages[j].text.splitlines()
            j_text = str(''.join(''.join(temp_line)))
            j_html = str(sorted_messages[j].get_attribute('innerHTML'))
            print(i_text,' - ', j_text, '\n', type(i_text), ' - ', type(j_text))
            if i_text==j_text:
                print('True')
                #cant see mess with a lot of photo
                # wait = WebDriverWait(driver, 10)
                # element = wait.until(EC.element_to_be_clickable(By.XPATH, '//div[@data-testid="{}"]'.format('msg-container')))
                # if '_3BK98' in j_html:
                print('True')
                try:
                    # document_root = html.document_fromstring(j_html)
                    # print(etree.tostring(document_root, encoding='unicode', pretty_print=True))
                    selected = sorted_messages[j].find_element(By.XPATH, '//div[@data-testid="{}"]'.
                                                               format('msg-container'))
                    selected1 = sorted_messages[j].find_element(By.XPATH, '//div[@class="{}"]'.
                                                               format('_3BK98'))
                    print("-", str(selected.get_attribute('class')))


                    # if msg_cont_class[0] in str(selected.get_attribute('class')):
                    print("solo photo")
                    try:
                        driver.execute_script("arguments[0].click();",
                                              sorted_messages[j].find_element(By.CLASS_NAME, '_3BK98'))
                        # pg.press('pagedown')
                    except Exception as e:
                        print(f"exception handled - {e}")
                        list_sum += 1
                        # element = WebDriverWait(driver, 10).until(
                        #                 EC.presence_of_element_located((By.ID, "myDynamicElement"))
                        #             )
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
print(list_sum)

# bs4_code.select_all_text(driver.page_source, message_class)
# bs4_code.select_photo_scr(driver.page_source, photo_class)
# sum_div = bs4_code.req_url(driver.page_source)
input()
driver.quit()