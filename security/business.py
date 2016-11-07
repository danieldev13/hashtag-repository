import jwt
import json

from settings import SettingsManager


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
        payload = json.loads(data.decode(SettingsManager.get_instance().get_application_settings.encoding))
        return encode(payload,
                      SettingsManager.get_instance().get_application_settings.key,
                      SettingsManager.get_instance().get_application_settings.algorithm)
    except Exception as err:
        raise err


def is_authenticated(token):
    try:
        decoded_token = decode_string(token,
                                      SettingsManager.get_instance().get_application_settings.key,
                                      SettingsManager.get_instance().get_application_settings.algorithm)

        return decoded_token is not None
    except Exception as err:
        raise err
