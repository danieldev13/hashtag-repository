import jwt
import json


key = u'secret-key'
default_algorithm = u'HS256'


def encode(payload, secret, algorithm):
    try:
        result = jwt.encode({'some': 'payload'}, secret, algorithm)
        return result
    except Exception as err:
        raise err


def decode(encoded, secret, algorithm):
    try:
        return jwt.decode(json.loads(encoded), secret, algorithm)
    except Exception as err:
        raise err


def get_token(payload):
    try:
        return encode(payload, key, default_algorithm)
    except Exception as err:
        raise err
