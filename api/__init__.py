from flask import Flask
from flask_restful import Api

from api import *

Logger.configure()

app = Flask(__name__)
api = Api(app)

api.add_resource(HashtagApi, "/api/hashtag/<int:id_hashtag>",
                 methods=['GET', 'DELETE'],
                 endpoint="api_hashtag_endpoint")
api.add_resource(HashtagListApi, "/api/hashtag/",
                 methods=['GET'],
                 endpoint="api_hashtag_endpoint_get_list")
api.add_resource(HashtagApi, "/api/hashtag/",
                 methods=['POST'],
                 endpoint="api_hashtag_endpoint_post")

if __name__ == "__main__":
    app.run(debug=False)
