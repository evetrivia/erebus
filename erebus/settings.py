

import os


class Config(object):
    """ Default config values. """
    
    DEBUG = False


class ProdConfig(Config):
    """ Production configuration. """
    
    MYSQL_HOST = os.environ.get('MYSQL_HOST')
    MYSQL_USER	= os.environ.get('MYSQL_USER')
    MYSQL_PASSWORD	= os.environ.get('MYSQL_PASSWORD')
    MYSQL_DB = os.environ.get('MYSQL_DB')


class DevConfig(Config):
    """ Development configuration. """
    
    DEBUG = True

    MYSQL_HOST = '127.0.0.1'
    MYSQL_USER	= 'vagrant'
    MYSQL_PASSWORD	= 'vagrant'
    MYSQL_DB = 'thanatos'

class C9Config(DevConfig):
    """ Development configuration for the C9 IDE """
    
    MYSQL_HOST = os.environ.get('IP')
    MYSQL_USER	= os.environ.get('C9_USER')
    MYSQL_PASSWORD	= ''
    MYSQL_DB = 'c9'