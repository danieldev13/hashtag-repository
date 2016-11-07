import jwt
import json


key = u'secret-key'
default_algorithm = u'HS256'
encoding = u'utf-8'


def encode(payload, secret, algorithm):
    try:
        result = jwt.encode(payload, secret, algorithm)
        return result
    except Exception as err:
        raise err


def decode(encoded, secret, algorithm):
    try:
        return jwt.decode(json.loads(encoded), secret, algorithm)
    except Exception as err:
        raise err


def decode_string(encoded, secret, algorithm):
    try:
        return jwt.decode(encoded, secret, algorithm)
    except Exception as err:
        raise err


def get_token(data):
    try:
        payload = json.loads(data.decode(encoding))
        return encode(payload, key, default_algorithm)
    except Exception as err:
        raise err


def is_authenticated(token):
    try:
        decoded_token = decode_string(token, key, default_algorithm)

        return decoded_token is not None
    except Exception as err:
        raise err
