import logging


class SettingsManager(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if SettingsManager.__instance is None:
            SettingsManager.__instance = object.__new__(cls)
            SettingsManager.__instance.__database_settings = DatabaseSettings()
            SettingsManager.__instance.__logging_settings = LoggingSettings()
            SettingsManager.__instance.__application_settings = ApplicationSettings()

        return SettingsManager.__instance

    @staticmethod
    def get_instance():
        return SettingsManager()

    @property
    def get_database_settings(self):
        return self.__database_settings

    @property
    def get_logging_settings(self):
        return self.__logging_settings

    @property
    def get_application_settings(self):
        return self.__application_settings


class DatabaseSettings:
    def __init__(self):
        self.__host = 'bolt://localhost:7687'
        self.__user = 'neo4j'
        self.__pwd = 'cerosneo4j'

    @property
    def host(self):
        return self.__host

    @property
    def user(self):
        return self.__user

    @property
    def password(self):
        return self.__pwd


class LoggingSettings:
    def __init__(self):
        self.__log_file = 'log/log.log'
        self.__log_format = '[%(asctime)s][%(levelname)s][%(message)s]'
        self.__log_level = logging.DEBUG

    @property
    def log_file(self):
        return self.__log_file

    @property
    def log_format(self):
        return self.__log_format

    @property
    def log_level(self):
        return self.__log_level


class ApplicationSettings:
    pass


class Logger:
    @staticmethod
    def configure():
        logging.basicConfig(filename=SettingsManager.get_instance().get_logging_settings.log_file,
                            level=SettingsManager.get_instance().get_logging_settings.log_level,
                            format=SettingsManager.get_instance().get_logging_settings.log_format)

    @staticmethod
    def error(message):
        logging.error(message)

    @staticmethod
    def info(message):
        logging.info(message)

    @staticmethod
    def critical(message, exception):
        logging.critical(message, exception)
