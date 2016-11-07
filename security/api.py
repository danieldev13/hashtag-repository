from flask import request
from flask_restful import Resource
from settings import SettingsManager
from business import get_token, is_authenticated
from adapters import adapt_critical, adapt_one_success


class SecurityApi(Resource):
    def get(self):
        try:
            token = get_token(request.data).decode(SettingsManager.get_instance().get_application_settings.encoding)

            return adapt_one_success(token)
        except Exception as err:
            return adapt_critical('Error: ' + str(err.args))

    def post(self):
        try:
            token = request.data.decode(SettingsManager.get_instance().get_application_settings.encoding)

            return adapt_one_success(is_authenticated(token))
        except Exception as err:
            return adapt_critical('Error: ' + str(err.args))
