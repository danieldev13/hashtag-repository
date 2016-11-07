from flask import Response
from settings import Logger
from entities import Hashtag


def adapt_success(data):
    try:
        result = '{"status": "OK", "total": ' \
                      + str(len(data)) + \
                      ', "data": [' + ','.join(data) + ']}\n'

        response = Response(result, status=200, mimetype='application/json')
        return response
    except Exception as ex:
        Logger.critical('There was an error while creating success response', ex)
        raise ex


def adapt_one_success(data):
    try:
        result = '{"status": "OK", "total": ' + \
                      ', "data": "' + data + '"}\n'

        response = Response(result, status=200, mimetype='application/json')
        return response
    except Exception as ex:
        Logger.critical('There was an error while creating success response', ex)
        raise ex


def adapt_error(message):
    try:
        result = '{"status": "error", "message":"' + message + '"}\n'
        response = Response(result, status=200, mimetype='application/json')
        return response
    except Exception as ex:
        Logger.critical('There was an error while creating error response', ex)
        raise ex


def adapt_critical(exception):
    try:
        result = '{"status": "critical", "message": "' + exception + '"}\n'
        response = Response(result, status=200, mimetype='application/json')
        return response
    except Exception as ex:
        Logger.critical('There was an error while creating critical response', ex)
        raise ex


def adapt_hashtag(data):
    try:
        hashtag = Hashtag()

        hashtag.id = data['id']
        hashtag.text = data['text']

        return hashtag
    except Exception as err:
        raise err
