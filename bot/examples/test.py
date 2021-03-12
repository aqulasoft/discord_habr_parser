import json

class Book():

    def __init__(self, pages: int, genre: str):
        self.pages = pages
        self.genre = genre

        self.cover = None
        self.author = None

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class Comics(Book):

    def __init__(self, pages: int, genre: str):
        super().__init__(pages, genre)
        self.image_count = 0

comics = Comics(123, 'veselo')

jsonstr = comics.toJSON()

dic = {
    "field1": 123,
    "field2": 456
}

dic['field1']

# seriallize
resstr = json.dumps(dic) # объект в строку

# resstr['field1']


print(resstr) # эт строка

# deseriallize
res2 = json.loads(resstr) # строка в объект


print(res2['field1'])
