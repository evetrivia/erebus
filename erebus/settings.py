

import os


class Config(object):
    """ Default config values. """
    
    DEBUG = False

    MYSQL_HOST = os.environ.get('MYSQL_HOST', '127.0.0.1')
    MYSQL_USER = os.environ.get('MYSQL_USER', 'vagrant')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'vagrant')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'thanatos')


class ProdConfig(Config):
    """ Production configuration. """


class DevConfig(Config):
    """ Development configuration. """
    
    DEBUG = True
