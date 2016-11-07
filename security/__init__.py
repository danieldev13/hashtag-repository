from flask import Flask
from flask_restful import Api

from settings import Logger
from api import *

Logger.configure()

app = Flask(__name__)
api = Api(app)

api.add_resource(SecurityApi, "/api/security/retrieve/",
                 endpoint="api_security_endpoint_get")

api.add_resource(SecurityApi, "/api/security/check/",
                 endpoint="api_security_endpoint_post")

if __name__ == "__main__":
    app.run(debug=False)
