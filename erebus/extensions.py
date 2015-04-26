

from flask.ext.restful import Api
from flask.ext.restful.utils.cors import crossdomain
api = Api(decorators=[crossdomain(origin='*')])


def register_extensions(app):
    """ Registers all relevant extensions. """

    api.init_app(app)

    return None