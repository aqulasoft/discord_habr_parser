import requests
from bs4 import BeautifulSoup

base_url = 'https://habrahabr.ru/post'


class Article:

    def __init__(self, title, text):
        self.title = title
        self.text = text

    def __str__(self):
        return f'{self.title}\n\n\n{self.text}'


def get_article_info(article_id: int):
    page = requests.get(f'{base_url}/{article_id}')

    soup = BeautifulSoup(page.text, 'html.parser')

    title = soup.find_all("span", class_="post__title-text")
    body = soup.find_all("div", id="post-content-body")

    if len(title) > 0:
        article = Article(title[0].text, body[0].text)
        print(article)


get_article_info(534136)
