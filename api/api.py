from flask_restful import Resource

from repositories import *
from adapters import *


class HashtagApi(Resource):

    def __init__(self):
        pass

    def get(self):
        try:
            result = []
            hashtags = get_hashtags()

            for receipt in hashtags:
                result.append(receipt.to_json())

            return adapt_success(result)
        except:
            return adapt_critical('Error')

    def post(self, hashtag):
        try:
            put_hashtag(hashtag)
        except:
            return adapt_critical('Error')


class SecurityApi(Resource):
    def get(self, phone):
        pass
