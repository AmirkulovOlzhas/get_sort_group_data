import time


def click(pg, click_c=1):
    for i in range(click_c):
        pg.click(913, 617, button='middle')


def taking_sorted_messages(driver, By, saved_number=0):
    messages = driver.find_element(
        By.XPATH, '//div[@class="{}"]'.format("n5hs2j7m oq31bsqd lqec2n0o eu5j4lnj")). \
        find_elements(By.XPATH, '//div[@data-id]')

    if int(saved_number) != 0:
        sm = []
        sum = 0
        for mes in messages:
            if '_1-lf9 _3mSPV' not in mes.get_attribute('innerHTML'):
                sum += 1
                sm.append(mes)
            if int(saved_number) == 0:
                if '_1-lf9 _3mSPV' in mes.get_attribute('innerHTML'):
                    sum += 1
                    sm.append(mes)
        return sm, sum
    else:
        return messages, len(messages)


def select(driver, By, xpath, class_name, text='NULL', click=0, ms=False):
    selected_element = driver.find_element(By.XPATH, xpath.format(class_name))
    if click == 1:
        selected_element.click()
    if text != 'NULL':
        print(text)
    time.sleep(0.1)
    # if ms:
    #     return 1
    # else:
    #     return 0


def write_to_file(message_list):
    r = open('text.txt', 'w', encoding='utf8')
    j = 0
    for i in message_list:
        j += 1
        r.write(i)
        if j != len(message_list):
            r.write('\n')
    r.close()
