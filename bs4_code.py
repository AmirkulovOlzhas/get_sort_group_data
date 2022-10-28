from bs4 import BeautifulSoup as bs

from config import message_class_list, list_p, chat, list_en


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


def number_check(div_mes, flag):
    if div_mes.get('data-id'):
        if flag == 0:
            List = list_p
        else:
            List = list_en
        for key, value in List.items():
            if value in div_mes.get('data-id'):
                return True


def req_url(url, key=0, flag=0):
    soup = bs(url, 'lxml')
    messages = soup.find('div', class_=chat).find_all('div')
    messages_list, sum = [], 0
    # print('messages len: {}'.format(len(messages)))
    for div_mes in messages:
        if div_mes.get('class'):
            i_class = " ".join(map(str, div_mes.get('class')))
        else:
            i_class = "+"
        if ("_1-lf9 _3mSPV" not in str(div_mes.find_all('div'))) & (i_class in message_class_list):
            # проверка номеров
            print("+")
            if number_check(div_mes, flag):
                sum += 1
                messages_list.append(div_mes.text)
                print(div_mes.text)
                if key == 1:
                    pass
                    # print(j, " - ", i.text)
    print('sum = {}'.format(sum))
    if key == 0:
        return sum
    else:
        return messages_list
