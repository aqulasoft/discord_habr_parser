import json
import os
import random
from pathlib import Path

from bot.encoder import MyEncoder
from bot.parser import Article


class XmlArticleSaver:

    def __init__(self, file_path, save_block):
        path = Path(file_path)
        self.absolute_path = path.parent.absolute()
        self.file_name = path.name
        self.save_block = save_block

        self.articles = []

        os.makedirs(self.absolute_path, exist_ok=True)
        print(f'Absolute: {self.absolute_path}. filename: {self.file_name}')

    def save_article(self, article: Article):
        self.articles.append(article)

        if len(self.articles) % self.save_block:
            self.write_all()

    def write_all(self):
        with open(f"{self.absolute_path}/{self.file_name}", "w", encoding='UTF-8') as file:
            json.dump(self.articles, file, cls=MyEncoder, indent=4, ensure_ascii=False)


article_saver = XmlArticleSaver('100articles.json', 10)

for i in range(1000):
    article_id = random.randint(100, 540000)

    article = Article.get_article_info(article_id)
    print(f"{i} [{article_id}]: {article}")

    if article is not None:
        article_saver.save_article(article)

article_saver.write_all()
