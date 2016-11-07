import json

from flask import request
from flask_restful import Resource

from repositories import *
from adapters import *


class HashtagApi(Resource):

    def __init__(self):
        pass

    def get(self, token):
        try:

            # if not is_authenticated(token):
            #     return adapt_error("Failed to authenticate token.")

            result = []
            hashtags = get_hashtags()

            for receipt in hashtags:
                result.append(receipt.to_json())

            return adapt_success(result)
        except Exception as err:
            return adapt_critical('Error: ' + str(err.args))

    def post(self):
        try:
            hashtag = adapt_hashtag(json.loads(request.data.decode('utf-8')))
            put_hashtag(hashtag)
        except Exception as err:
            return adapt_critical('Error: ' + str(err.args))
