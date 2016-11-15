from repositories import *
from logger import Logger


def get_hashtags():
    try:
        return retrieve()
    except Exception as err:
        Logger.critical('There was an error while getting hashtag list.', err)
        raise err


def get_hashtag(id_hashtag):
    try:
        return retrieve_one(id_hashtag)
    except Exception as err:
        Logger.critical('There was an error while getting hashtag with id {0}.'.format(id_hashtag), err)
        raise err


def put_hashtag(hashtag):
    try:
        create(hashtag)
    except Exception as err:
        Logger.critical('There was an error while saving hashtag {0}.'.format(hashtag.text), err)
        raise err


def delete_hashtag(id_hashtag):
    try:
        delete(id_hashtag)
    except Exception as err:
        Logger.critical('There was an error while deleting hashtag with id {0}.'.format(id_hashtag), err)
        raise err


def check_token(token):
    try:
        pass
    except Exception as err:
        raise err
