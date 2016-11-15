def build_put_query(hashtag):
    try:
        query = "CREATE(h:Hashtag{{id: {0} ,text:'{1}'}})".format(hashtag.id, hashtag.text)

        return query
    except Exception as err:
        raise err


def build_get_query():
    try:
        query = "MATCH(h:Hashtag) RETURN h"

        return query
    except Exception as err:
        raise err


def build_get_one_query(id_hashtag):
    try:
        query = "MATCH(h:Hashtag) WHERE h.id = {0} RETURN h".format(id_hashtag)

        return query
    except Exception as err:
        raise err


def build_delete_query(id_hashtag):
    try:
        query = "MATCH(h:Hashtag) WHERE h.id = {0} DELETE h".format(id_hashtag)

        return query
    except Exception as err:
        raise err
