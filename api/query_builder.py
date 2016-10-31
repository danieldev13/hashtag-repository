def build_put_query(hashtag):
    try:
        query = "CREATE(h:Hashtag{{id: {0} ,text:'{1}'}})"\
            .format(hashtag.id, hashtag.hashtag_message)

        return query
    except Exception as err:
        raise err


def build_get_query():
    try:
        query = "MATCH(h:Hashtag) RETURN h"

        return query
    except Exception as err:
        raise err
