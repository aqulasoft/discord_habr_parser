import datetime

import requests
from bs4 import BeautifulSoup

base_url = 'https://habrahabr.ru/post'

class Article:

    def __init__(self, article_id, title, text, date=None):
        self.article_id = article_id
        self.title = title
        self.text = text

        if date is None:
            self.date = datetime.datetime.now()
        else:
            self.date = datetime.datetime.strptime(date, '%d.%m.%Y %H.%M.%S')

    def __str__(self):
        return f'{self.title}\n\n\n{self.text}'

    @staticmethod
    def get_article_info(article_id: int):
        page = requests.get(f'{base_url}/{article_id}')

        soup = BeautifulSoup(page.text, 'html.parser')

        title = soup.find_all("span", class_="post__title-text")
        body = soup.find_all("div", id="post-content-body")

        if len(title) > 0:
            return Article(article_id, title[0].text, body[0].text)

        return None


#test
#get_article_info(534136)
