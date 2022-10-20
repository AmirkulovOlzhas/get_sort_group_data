import time


def taking_sorted_messages(driver, By, solo=0, check=False):
    messages = driver.find_element(
        By.XPATH, '//div[@class="{}"]'.format("n5hs2j7m oq31bsqd lqec2n0o eu5j4lnj")). \
        find_elements(By.XPATH, '//div[@data-id]')
    sm = []
    sum=0
    # print('len messages: ', len(messages))
    for mes in messages:
        # print(mes.get_attribute('innerHTML'))
        if '_1-lf9 _3mSPV' not in mes.get_attribute('innerHTML'):
            sum+=1
            sm.append(mes)
    if check:
        # print("if 30: ", sm[solo].get_attribute('innerHTML'))
        return sm[solo]
    else:
        return sm, sum


def print_time(ttic, ttoc, text='?'):
    print("used time for {}: {} sec".format(text, (ttic - ttoc)))
    return time.time()


def select(driver, By, xpath, class_name, text='NULL', click=0, ms=False):
    selected_element = driver.find_element(By.XPATH, xpath.format(class_name))
    if click == 1:
        selected_element.click()
    if text != 'NULL':
        print(text)
    time.sleep(0.5)

    if ms:
        return 1
    else:
        return 0


def write_to_file(message_list):
    r = open('text.txt', 'w', encoding='utf8')
    j=0
    for i in message_list:
        j+=1
        r.write(i)
        if j != len(message_list):
            r.write('\n')
    r.close()

