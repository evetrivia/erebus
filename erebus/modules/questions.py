

from flask.ext.restful import Resource


class Test(Resource):
    """ TESTING """
    
    def get(self):
        return {}
    

def register_apis(api):
    """ Registers the API resources defined in this file with the app in it's application factory. """
    
    api.add_resource(Test, '/test/')