import sys, os
import warnings

from bs4 import BeautifulSoup as bs
from config import contacts_dict, chat, not_select_messages, contact_place
import numpy as np

warnings.simplefilter(action='ignore', category=FutureWarning)


def number_list_append(div_mes, flag, messages_list, sum, saved_number):
    if number_check(div_mes, flag) == saved_number:
        text = ''.join(div_mes.text.splitlines())
        # print(div_mes.text.split)
        # print('+', '---'.join(div_mes.text.splitlines()))
        sum += 1
        if text.count(':') < 3:
            if text[-5:] == text[-10:-5]:
                # нужна правильная формула
                messages_list = np.append(messages_list, text[:-5])
            else:
                messages_list = np.append(messages_list, text)
        else:
            messages_list = np.append(messages_list, text)
    return messages_list, sum


def number_check(div_mes, flag):
    if div_mes.get('data-id'):
        this_list = contacts_dict[flag]
        for key, value in this_list.items():
            if value in div_mes.get('data-id'):
                return 1
        return 0


def count_mes_in_chat(url):
    return len(bs(url, 'lxml').find('div', class_=chat).find_all('div'))


def req_url(url, flag=0, saved_number=0):
    # np после изменения
    try:
        messages = bs(url, 'lxml').find('div', class_=chat).find_all('div')
        messages_list, sum = np.array([]), 0
        for div_mes in messages:
            if div_mes.get('class'):
                classes = np.array([])
                check = 0
                for element in div_mes.find_all(class_=True):
                    classes = np.append(classes, element["class"])
                classes = classes[classes != None]

                if saved_number == 1:
                    if not any(wrong_class in classes for wrong_class in not_select_messages):
                        if '_1-lf9' in classes:
                            check = 1

                else:
                    if '_1-lf9' in classes and 'NQl4z' not in classes:
                        temp_value = None
                        if flag in [1, 2]:
                            temp_value = contact_place[flag]
                        if temp_value:
                            if div_mes.text[0:4] != temp_value:
                                check = 1
                        else:
                            check = 1
                if check == 1:
                    messages_list, sum = number_list_append(
                        div_mes, flag, messages_list, sum=sum, saved_number=saved_number)

        messages.clear()
        print('messages to select = {}'.format(sum))
        return messages_list
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno, e)
