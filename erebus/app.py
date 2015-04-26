

from flask import Flask

from erebus.settings   import DevConfig
from erebus.extensions import register_extensions
from erebus.modules    import register_apis


def create_app(config_object=DevConfig):
    """  application factory. """

    app = Flask(__name__)
    app.config.from_object(config_object)
    
    register_apis()
    register_extensions(app)

    return app