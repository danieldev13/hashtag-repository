import logging
from settings import SettingsManager


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
