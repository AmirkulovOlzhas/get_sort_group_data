from bs4 import BeautifulSoup as bs
from config import message_class_list, message_class_list_with_text, list_p

#git test
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
        print(i.get('data-id'))
        for key, value in list_p.items():
            if value in i.get('data-id'):
                print(key)
                return 1


def req_url(url):
    soup = bs(url, 'lxml')
    messages = soup.find('div', class_='n5hs2j7m oq31bsqd gx1rr48f qh5tioqs').find_all('div')
    sum = 0
    print('messages len: {}'.format(len(messages)))
    for i in messages:
        if i.get('class'):
            i_class = " ".join(map(str, i.get('class')))
        else:
            i_class = " "
        if i_class in message_class_list:
            if i_class in message_class_list_with_text:
                if i_class.find('img'):
                    number_check(i)
                    sum+=1
            else:
                number_check(i)
                sum+=1

    print('sum = {}'.format(sum))
