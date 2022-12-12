from bs4 import BeautifulSoup as bs
from config import message_class_list, list_p, chat, list_en, \
                   list_ab, list_tbo, text_message, contact_list


def number_list_append(div_mes, flag, messages_list, sum, saved_number, key=0):
    if number_check(div_mes, flag) == saved_number:
        sum += 1
        if (key != 0) & (div_mes.text.count(':') < 3):
            if div_mes.text[-5:] == div_mes.text[-10:-5]:
                messages_list.append(div_mes.text[:-5])
            else:
                messages_list.append(div_mes.text)
        else:
            messages_list.append(div_mes.text)
    return messages_list, sum


def number_check(div_mes, flag):
    if div_mes.get('data-id'):
        check, this_list = 0, 0
        # убрать условия со словарем
        # this_list = contact_list[flag]
        match flag:
            case 0:
                this_list = list_p
            case 1:
                this_list = list_en
            case 2:
                this_list = list_ab
            case 3:
                this_list = list_tbo
        # print(this_list)
        # print(type(this_list))
        for key, value in this_list.items():
            if value in div_mes.get('data-id'):
                check = 1
                break
        return check


def req_url(url, key=0, flag=0, saved_number=0):
    soup = bs(url, 'lxml')
    if soup.find('div', class_=chat):
        messages = soup.find('div', class_=chat).find_all('div')
    if key == 0:
        return len(messages)
    else:
        messages_list, sum = [], 0
        date_list = []
        for div_mes in messages:
            if div_mes.get('class'):
                i_class = " ".join(map(str, div_mes.get('class')))
                # number check
                if saved_number == 1:
                    classes = []
                    for element in div_mes.find_all(class_=True):
                        classes.extend(element["class"])
                    # if (text_message not in str(div_mes.find_all('div'))) & (i_class in message_class_list):
                    if all(a not in classes for a in
                           [text_message, '_36Yw-', '_36Yw- _18q-J', '_2JmX4', '_1-FMR _15WYQ focusable-list-item',
                            '_2BJ4G', '_3mSPV', '_25eIs']) & (i_class in message_class_list):
                        messages_list, sum = number_list_append(
                            div_mes, flag, messages_list, sum=sum, saved_number=saved_number, key=key)
                    if '_1-FMR _15WYQ focusable-list-item' in classes:
                        if 'Сообщения' not in div_mes.text:
                            date_list.append(div_mes.text)
                else:
                    if i_class in message_class_list:
                        messages_list, sum = number_list_append(
                            div_mes, flag, messages_list, sum=sum, saved_number=saved_number, key=key)

        print('\nmessages to select = {}'.format(sum))
        print(date_list)
        return messages_list
