from bs4 import BeautifulSoup as bs
from config import message_class_list, list_p, chat, list_en, list_ab, text_message


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
        match flag:
            case 0:
                this_list = list_p
            case 1:
                this_list = list_en
            case 2:
                this_list = list_ab
        for key, value in this_list.items():
            if value in div_mes.get('data-id'):
                check = 1
                break
        return check


def req_url(url, key=0, flag=0, saved_number=0):
    soup = bs(url, 'lxml')
    messages = soup.find('div', class_=chat).find_all('div')
    if key == 1:
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
                        div_mes, flag, messages_list, sum=sum, saved_number=saved_number, key=key)
            else:
                if i_class in message_class_list:
                    messages_list, sum = number_list_append(
                        div_mes, flag, messages_list, sum=sum, saved_number=saved_number, key=key)

        print('\nmessages to select = {}'.format(sum))
        return messages_list
    else:
        return len(messages)


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
    print('got span: {}'.format(len(got_span)))
