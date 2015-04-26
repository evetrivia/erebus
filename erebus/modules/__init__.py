

from erebus.extensions import api


def register_apis():
    from erebus.modules.questions import register_apis
    register_apis(api)