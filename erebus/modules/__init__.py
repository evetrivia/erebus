

from erebus.extensions import api


def register_apis():
    from erebus.modules.root import register_apis
    register_apis(api)
    
    from erebus.modules.questions import register_apis
    register_apis(api)