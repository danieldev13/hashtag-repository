from flask import Flask
from flask_restful import Api

from api import *

Logger.configure()

app = Flask(__name__)
api = Api(app)

api.add_resource(HashtagApi, "/api/hashtag/",
                 endpoint="api_endpoint_get")

if __name__ == "__main__":
    app.run(debug=False)
