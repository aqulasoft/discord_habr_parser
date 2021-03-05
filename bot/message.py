import json

class Message():

    def __init__(self, user: str, text: str):
        self.user = user
        self.text = text

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=2)


def decode_message(dct):
    return Message(dct['user'], dct['text'])


message1 = Message('forichok', 'veselo')

data = message1.toJSON()

loaded_message = json.loads(data, object_hook=decode_message)

print(loaded_message.user)
