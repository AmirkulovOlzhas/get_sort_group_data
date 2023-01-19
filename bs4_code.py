from bs4 import BeautifulSoup as bs
from config import chat


def count_mes_in_chat(url):
    return len(bs(url, 'lxml').find('div', class_=chat).find_all('div'))
