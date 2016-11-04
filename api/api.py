from flask import request
from flask_restful import Resource

from repositories import *
from adapters import *
from security import get_token


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
    def get(self):
        try:
            token = get_token(request.data).decode('utf-8')

            return adapt_one_success(token)
        except Exception as err:
            return adapt_critical('Error' + err)
