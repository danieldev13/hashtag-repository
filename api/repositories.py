from neo4j.v1 import GraphDatabase
from neo4j.v1 import basic_auth

from infrastructure import SettingsManager
from query_builder import *
from entities import Hashtag

driver = GraphDatabase.driver(SettingsManager.get_instance().get_database_settings.host,
                              auth=basic_auth(SettingsManager.get_instance().get_database_settings.user,
                              SettingsManager.get_instance().get_database_settings.password))


def get_hashtags():
    result = []
    session = driver.session()

    try:
        query = build_get_query()
        data = session.run(query)

        for item in data:
            hashtag = Hashtag()
            hashtag.id = item['r']['id']
            hashtag.hashtag_message = item['r']['text']

            result.append(hashtag)

        return result
    except Exception as err:
        raise err
    finally:
        session.close()


def put_hashtag(hashtag):
    session = driver.session()

    try:
        query = build_put_query(hashtag)
        session.run(query)
    except Exception as err:
        raise err
    finally:
        session.close()
