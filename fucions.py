import time


def click(pg, click_c=1):
    for i in range(click_c):
        pg.click(913, 617, button='middle')


def taking_sorted_messages(driver, By, saved_number=0):
    messages = driver.find_element(
        By.XPATH, '//div[@class="{}"]'.format("n5hs2j7m oq31bsqd lqec2n0o eu5j4lnj")). \
        find_elements(By.XPATH, '//div[@data-id]')
    sm = []
    if int(saved_number) != 0:
        for mes in messages:
            if '_1-lf9 _3mSPV' not in mes.get_attribute('innerHTML'):
                sm.append(mes)
        return sm
    else:
        return messages


def select(driver, By, xpath, class_name, text='NULL', clicked=0):
    selected_element = driver.find_element(By.XPATH, xpath.format(class_name))
    if clicked == 1:
        selected_element.click()
    if text != 'NULL':
        print(text)
    time.sleep(0.1)


def write_to_file(message_list):
    r = open('text.txt', 'w', encoding='utf8')
    for i in range(len(message_list)):
        r.write(message_list[i])
        if i+1 != len(message_list):
            r.write('\n')
    r.close()
