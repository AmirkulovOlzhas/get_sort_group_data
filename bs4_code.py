import time

from bs4 import BeautifulSoup as bs
from config import chat, contacts_dict, chat, not_select_messages, message_class
import numpy as np


def number_list_append(div_mes, flag, messages_list, sum, saved_number, key=0):
    if number_check(div_mes, flag) == saved_number:
        sum += 1
        if (key != 0) & (div_mes.text.count(':') < 3):
            if div_mes.text[-5:] == div_mes.text[-10:-5]:
                messages_list = np.append(messages_list, div_mes.text[:-5])
            else:
                messages_list = np.append(messages_list, div_mes.text)
        else:
            messages_list = np.append(messages_list, div_mes.text)
    return messages_list, sum


def number_check(div_mes, flag):
    if div_mes.get('data-id'):
        this_list = contacts_dict[flag]
        for key, value in this_list.items():
            if value in div_mes.get('data-id'):
                return 1
        return 0


def req_url(url, key=0, flag=0, saved_number=0):
    # np
    messages = bs(url, 'lxml').find('div', class_=chat).find_all('div')
    if key == 0:
        return len(messages)
    else:
        messages_list, sum = np.array([]), 0
        for div_mes in messages:
            if div_mes.get('class'):
                # np
                classes = []
                for element in div_mes.find_all(class_=True):
                    classes.append(element["class"])
                classes = list(filter(None, classes))
                # проверка сохранен ли контакт, сохранение сообщений которые можно выделить
                if saved_number == 1:
                    if any((not any(wrong_class in un_class for wrong_class in not_select_messages)) &
                           ('_1-lf9' in un_class) for un_class in classes):
                        messages_list, sum = number_list_append(
                            div_mes, flag, messages_list, sum=sum, saved_number=saved_number, key=key)
                else:
                    i_class = " ".join(map(str, div_mes.get('class')))
                    if i_class[-6:] == message_class:
                        messages_list, sum = number_list_append(
                            div_mes, flag, messages_list, sum=sum, saved_number=saved_number, key=key)
        print('messages to select = {}'.format(sum))
        return messages_list
