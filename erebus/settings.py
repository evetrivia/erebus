

class Config(object):
    """ Default config values. """
    DEBUG = False


class DevConfig(Config):
    """ Development configuration. """
    DEBUG = True
    SECRET_KEY = 'ThisIsJustTheDevKeyAndPrmesFromSomethingElseYBA*Sga78siTD&*SA%D&A*^STD&A^ISDAS'


class C9Config(DevConfig):
    """ Development configuration for the C9 IDE """