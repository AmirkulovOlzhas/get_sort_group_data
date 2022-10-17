from bs4 import BeautifulSoup as bs

from config import message_class_list, list_p, chat


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


def number_check(i):
    if i.get('data-id'):
        # print(i.get('data-id'))
        for key, value in list_p.items():
            if value in i.get('data-id'):
                # print(key)
                return 1


def req_url(url, key=0):
    j = 0
    soup = bs(url, 'lxml')
    messages = soup.find('div', class_=chat).find_all('div')
    sum = 0
    messages_list = []
    # print('messages len: {}'.format(len(messages)))
    for i in messages:
        if i.get('class'):
            i_class = " ".join(map(str, i.get('class')))
        else:
            i_class = " "
        if ("_1-lf9 _3mSPV" not in str(i.find_all('div'))) & (i_class in message_class_list):
            number_check(i)
            sum += 1
            messages_list.append(i.text)
            if key == 1:
                j += 1
                print(j, " - ", i.text)
    print('sum = {}'.format(sum))
    if key == 0:
        return sum
    else:
        return sum, messages_list
