from bs4 import BeautifulSoup as bs
from config import message_class_list, list_p, chat, list_en, list_ab, text_message


def number_list_append(div_mes, flag, messages_list, sum, saved_number):
    if number_check(div_mes, flag) == int(saved_number):
        sum += 1
        messages_list.append(div_mes.text)
    return messages_list, sum


def number_check(div_mes, flag):
    if div_mes.get('data-id'):
        check = 0
        if int(flag) == 0:
            this_list = list_p
        elif int(flag) == 1:
            this_list = list_en
        else:
            this_list = list_ab
        for key, value in this_list.items():
            # print(value, div_mes.get('data-id'))
            if value in div_mes.get('data-id'):
                check += 1
        return check


def req_url(url, key=0, flag=0, saved_number=0):
    soup = bs(url, 'lxml')
    messages = soup.find('div', class_=chat).find_all('div')
    messages_list, sum = [], 0
    for div_mes in messages:
        if div_mes.get('class'):
            i_class = " ".join(map(str, div_mes.get('class')))
        else:
            i_class = "+"
        # number check
        if saved_number == 1:
            if (text_message not in str(div_mes.find_all('div'))) & (i_class in message_class_list):
                messages_list, sum = number_list_append(
                                     div_mes, flag, messages_list, sum=sum, saved_number=saved_number)
        else:
            if i_class in message_class_list:
                messages_list, sum = number_list_append(
                                     div_mes, flag, messages_list, sum=sum, saved_number=saved_number)

    print('sum = {}'.format(sum))
    if key == 0:
        return sum
    else:
        return messages_list


def select_all_text(url, class_name):
    soup = bs(url, 'html.parser')
    try:
        got_span = soup.find_all("span", {"class": "{}".format(class_name)})
    except IndexError:
        got_span = 'null'

    for span in got_span:
        print(span.text)
    print(got_span)


def select_photo_scr(url, class_name):
    soup = bs(url, 'html.parser')
    try:
        got_span = soup.find_all("img", {"class": "{}".format(class_name)})
    except IndexError:
        got_span = 'null'

    # for span in got_span:
    #     print(span.text)
    print('got span: {}'.format(len(got_span)))
