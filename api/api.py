import json

from flask import request
from flask_restful import Resource

from repositories import *
from adapters import *


class HashtagApi(Resource):

    def __init__(self):
        pass

    def get(self, id_hashtag):
        try:

            token = request.headers.get('auth-token')
            hashtag = get_hashtag(id_hashtag)

            return adapt_one_success(hashtag.to_json())
        except Exception as err:
            return adapt_critical('Error: ' + str(err.args))

    def post(self):
        try:
            hashtag = adapt_hashtag(json.loads(request.data.decode('utf-8')))
            put_hashtag(hashtag)
        except Exception as err:
            return adapt_critical('Error: ' + str(err.args))

    def delete(self, id):
        try:
            pass
        except Exception as err:
            return adapt_critical('Error: ' + str(err.args))


class HashtagListApi(Resource):
    def __init__(self):
        pass

    def get(self):
        try:

            token = request.headers.get('auth-token')
            result = []
            hashtags = get_hashtags()

            for receipt in hashtags:
                result.append(receipt.to_json())

            return adapt_success(result)
        except Exception as err:
            return adapt_critical('Error: ' + str(err.args))