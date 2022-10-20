import time

import pyautogui as pg
from selenium import webdriver
from selenium.webdriver.common.by import By
from fucions import taking_sorted_messages, print_time, select, write_to_file
from bs4_code import req_url
from config import contact, archive, select_ico, argument1, argument2,\
    select_ico2,select_ico3,select_ico_input,select_ico4


tic = time.time()
options = webdriver.ChromeOptions()
options.add_argument(argument1)
options.add_argument(argument2)

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
n=''
sum = 0

for i in r:
    for j in range(len(sorted_messages)):
        if(sorted_messages[j])!='none':
            temp_line = sorted_messages[j].text.splitlines()
            # n1 = n
            n = ''.join(temp_line)
            k = sorted_messages[j].get_attribute('innerHTML')
            # if 'img' in sorted_messages[j].get_attribute('innerHTML'):
            #     if str(''.join(i.splitlines())) == 'Фото 17 Мкр Мухаббат07:59':
            #         print('{}-'.format(sum),str(''.join(n)))
            #         sum+=1

            # print(sorted_messages[j].get_attribute('innerHTML'))
            # print(str(''.join(i.splitlines())), ' - ', str(''.join(n)))
            if (str(''.join(n)) in str(''.join(i.splitlines()))):
                if 'img' in k:
                    if '_3BK98' in k:
                        # print(str(sorted_messages[j].get_attribute('innerHTML')))
                        if "_1-lf9 _3mSPV" not in k:
                            try:
                                # print(i.splitlines()[0], ' - ', n)
                                # print('+', sorted_messages[j].get_attribute('innerHTML'))
                                # selected worked with select_ico
                                selected = sorted_messages[j].find_element(By.XPATH, '//div[@class="{}"]'.
                                                                           format(select_ico))
                                # selected.click()
                                driver.execute_script("arguments[0].click();", selected)
                                time.sleep(1)
                                print(k)
                                sorted_messages[j] = 'none'#taking_sorted_messages(driver, By, j, True)
                                sum+=1
                                break
                            except Exception as e:
                                print("-----------------------\nwrong: {}".format(e))
                                print(sorted_messages[j])
                                print(k,'\n--------------------')
                            finally:
                                print(str(''.join(n)), ' - ',  str(''.join(i.splitlines())))
                        else:
                            print("---")


print("sum = {}".format(sum))
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
#         # select(driver, By, '//span[@class="{}"]', message_class, ms=True)

tic = print_time(tic, time.time(), "array2")

# bs4_code.select_all_text(driver.page_source, message_class)
# bs4_code.select_photo_scr(driver.page_source, photo_class)
# sum_div = bs4_code.req_url(driver.page_source)
input()
driver.quit()