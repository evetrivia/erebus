

from flask.ext.restful import Api
from flask.ext.restful.utils.cors import crossdomain
api = Api(decorators=[crossdomain(origin='*')])

from flask.ext.mysqldb import MySQL
mysql = MySQL()


def register_extensions(app):
    """ Registers all relevant extensions. """

    api.init_app(app)
    mysql.init_app(app)

    return None
