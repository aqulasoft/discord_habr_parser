from json import JSONEncoder

from bot.parser import Article


class MyEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Article):
            return {'id': obj.article_id, 'date': obj.date.strftime("%d.%m.%Y %H.%M.%S"), 'title': obj.title,
                    'text': obj.text}
