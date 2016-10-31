from flask import Response

from infrastructure import Logger


def adapt_success(data):
    try:
        result = '{"status": "OK", "total": ' \
                      + str(len(data)) + \
                      ', "data": [' + ','.join(data) + ']}'

        response = Response(result, status=200, mimetype='application/json')
        return response
    except Exception as ex:
        Logger.critical('There was an error while creating success response', ex)
        raise ex


def adapt_one_success(data):
    try:
        result = '{"status": "OK", "total": ' \
                      + str(len(data)) + \
                      ', "data": ' + data + '}'

        response = Response(result, status=200, mimetype='application/json')
        return response
    except Exception as ex:
        Logger.critical('There was an error while creating success response', ex)
        raise ex


def adapt_error(message):
    try:
        result = '{"status": "error", "message":"' + message + '"}'
        response = Response(result, status=200, mimetype='application/json')
        return response
    except Exception as ex:
        Logger.critical('There was an error while creating error response', ex)
        raise ex


def adapt_critical(exception):
    try:
        result = '{"status": "critical", "message": "' + exception + '"}'
        response = Response(result, status=200, mimetype='application/json')
        return response
    except Exception as ex:
        Logger.critical('There was an error while creating critical response', ex)
        raise ex
