

import os


class Config(object):
    """ Default config values. """
    
    DEBUG = False


class DevConfig(Config):
    """ Development configuration. """
    
    DEBUG = True
    SECRET_KEY = 'ThisIsJustTheDevKeyAndPrmesFromSomethingElseYBA*Sga78siTD&*SA%D&A*^STD&A^ISDAS'

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