import json


class Hashtag:

    def __init__(self):
        self.id = None
        self.hashtag_message = None

    def to_json(self):
        return json.dumps(self.__dict__, ensure_ascii=False)
