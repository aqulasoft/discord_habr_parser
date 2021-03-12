import os
import random
from pathlib import Path

from bot.parser import Article


class XmlArticleSaver:
    def __init__(self, file_path):
        path = Path(file_path)
        self.absolute_path = path.parent.absolute()
        self.file_name = path.name

        print(f'Absolute: {self.absolute_path}. filename: {self.file_name}')
        os.makedirs(self.absolute_path, exist_ok=True)

    def save_article(self, article: Article):

        with open(f"{self.absolute_path}/{self.file_name}", "a", encoding='UTF-8') as file:
            file.write(str(article))


article_saver = XmlArticleSaver('C:\\Users\\woipot\\Downloads\\Копирайтик.txt')

for i in range(1):
    article_id = random.randint(100, 540000)

    article = Article.get_article_info(article_id)
    print(f"{i} [{article_id}]: {article}")

    if article is not None:
        article_saver.save_article(article)
