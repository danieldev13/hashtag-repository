from flask import Flask
from flask_restful import Api

from api import *

Logger.configure()

app = Flask(__name__)
api = Api(app)

api.add_resource(HashtagApi, "/api/hashtag/<token>",
                 endpoint="api_hashtag_endpoint_get")
api.add_resource(HashtagApi, "/api/hashtag/create/",
                 endpoint="api_hashtag_endpoint_post")

api.add_resource(SecurityApi, "/api/security/",
                 endpoint="api_security_endpoint_get")

if __name__ == "__main__":
    app.run(debug=False)
