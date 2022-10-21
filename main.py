import time

import pyautogui as pg
from lxml import etree, html
from selenium import webdriver
from selenium.webdriver.common.by import By
from fucions import taking_sorted_messages, print_time, select, write_to_file
from bs4_code import req_url
from config import contact, archive, select_ico, argument1, argument2,\
    select_ico2,select_ico3,select_ico_input,select_ico4


tic = time.time()
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
tic = print_time(tic, time.time(), "begin")

# выбор контакта
select(driver, By, '//span[@title="{}"]', contact, "contact opened", 1)

pg.click(913, 617)
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
tic = print_time(tic, time.time(), "step2")

message_list = req_url(driver.page_source, key=1)
write_to_file(message_list)

select(driver, By, '//div[@class="{}"]', '_28_W0', click=1)  # click menu
select(driver, By, '//div[@aria-label="{}"]', 'Выбрать сообщения', click=1)
tic = print_time(tic, time.time(), "selects")

sorted_messages, sum = taking_sorted_messages(driver, By)
print('len sorted_m: ', len(sorted_messages), ' - ', sum)

tic = print_time(tic, time.time(), "array1")

r = open('text.txt', 'r', encoding='utf8')
j_text= ''
sum = 0

for i in r:
    for j in range(len(sorted_messages)):
        i_text = str(''.join(i.splitlines()))
        if(sorted_messages[j])!='none':
            temp_line = sorted_messages[j].text.splitlines()
            j_text = str(''.join(''.join(temp_line)))
            j_html = str(sorted_messages[j].get_attribute('innerHTML'))
            # print(sorted_messages[j].get_attribute('innerHTML'))
            # print(str(''.join(i.splitlines())), ' - ', str(''.join(n)))
            if (j_text in i_text):
                if 'img' in j_html:
                    if '_3BK98' in j_html:
                        # print(str(sorted_messages[j].get_attribute('innerHTML')))
                        if "_1-lf9 _3mSPV" not in j_html:
                            if '_22Msk' not in j_html:
                                # sorted_messages[j].find_element(By.XPATH, '//')
                                try:
                                    # print(i.splitlines()[0], ' - ', n)
                                    print('+', j_html)
                                    # selected worked with select_ico
                                    document_root = html.document_fromstring(j_html)
                                    print(etree.tostring(document_root, encoding='unicode', pretty_print=True))
                                    selected = sorted_messages[j].find_element(By.XPATH, '//div[@data-testid="{}"]'.
                                                                               format('msg-container'))
                                    # selected = sorted_messages[j].find_element(By.XPATH, '//div[@class="{}"]'.
                                    #                                            format('_22Msk'))
                                    selected1 = sorted_messages[j].find_element(By.XPATH, '//div[@class="{}"]'.
                                                                               format('_3BK98'))
                                    # selected.click()
                                    print('selected: ',selected.get_attribute('innerHTML'))
                                    if 'image' in selected.get_attribute('innerHTML'):
                                        print("***")
                                        driver.execute_script("arguments[0].click();", selected1)
                                    time.sleep(0.3)
                                    print(j_html)
                                    sorted_messages[j]='none'
                                    # sorted_messages.remove(j)#taking_sorted_messages(driver, By, j, True)
                                    sum+=1
                                    break
                                except Exception as e:
                                    print("-----------------------\nwrong: {}".format(e))
                                    print(j_html)
                                finally:
                                    print(j_text, ' - ', i_text, '\n--------------------')
                        else:
                            print("---")

print("sum = {}".format(sum))

tic = print_time(tic, time.time(), "array2")

# bs4_code.select_all_text(driver.page_source, message_class)
# bs4_code.select_photo_scr(driver.page_source, photo_class)
# sum_div = bs4_code.req_url(driver.page_source)
input()
driver.quit()