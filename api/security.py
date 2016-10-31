import jwt


def encode(payload, secret, algorithm):
    try:
        return jwt.encode(payload, secret, algorithm)
    except Exception as err:
        return err


def decode(encoded, secret, algorithm):
    try:
        return jwt.decode(encoded, secret, algorithm)
    except Exception as err:
        return err
