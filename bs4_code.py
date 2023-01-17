import time
import sys, os
import warnings

from bs4 import BeautifulSoup as bs
from config import chat, contacts_dict, chat, not_select_messages, message_class
import numpy as np

warnings.simplefilter(action='ignore', category=FutureWarning)


def number_list_append(div_mes, flag, messages_list, sum, saved_number, key=0):
    if number_check(div_mes, flag) == saved_number:
        text = ''.join(div_mes.text.splitlines())
        # print(div_mes.text.split)
        # print('+', '---'.join(div_mes.text.splitlines()))
        sum += 1
        if (key != 0) & (text.count(':') < 3):
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


def req_url(url, key=0, flag=0, saved_number=0):
    # np послд изменения
    try:
        messages = bs(url, 'lxml').find('div', class_=chat).find_all('div')
        if key == 0:
            temp = len(messages)
            messages = None
            return temp
        else:
            messages_list, sum = np.array([]), 0
            for div_mes in messages:
                if div_mes.get('class'):
                    classes = np.array([])
                    for element in div_mes.find_all(class_=True):
                        classes = np.append(classes, element["class"])
                    classes = classes[classes != None]
                    # проверка сохранен ли контакт, сохранение сообщений которые можно выделить
                    if saved_number == 1:
                        if not any(wrong_class in classes for wrong_class in not_select_messages):
                            if '_1-lf9' in classes:
                                messages_list, sum = number_list_append(div_mes, flag, messages_list, sum=sum,
                                                                        saved_number=saved_number, key=key)
                    else:
                        if '_1-lf9' in classes and 'NQl4z' not in classes:
                            # !!!!!
                            temp_value = None
                            if flag == 1:
                                temp_value = 'Енб-'
                            elif flag == 2:
                                temp_value = 'Абай'
                            if temp_value:
                                if div_mes.text[0:4] != temp_value:
                                    messages_list, sum = number_list_append(
                                        div_mes, flag, messages_list, sum=sum, saved_number=saved_number, key=key)
                            else:
                                messages_list, sum = number_list_append(
                                    div_mes, flag, messages_list, sum=sum, saved_number=saved_number, key=key)
                    classes = None
            messages = None
            print('messages to select = {}'.format(sum))
            return messages_list
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno, e)
