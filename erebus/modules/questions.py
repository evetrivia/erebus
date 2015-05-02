

from flask.ext.restful import Resource

from erebus.extensions import mysql
from thanatos.questions.universe import BorderingRegionsQuestion


class Test(Resource):
    """ TESTING """
    
    def get(self):
        brq = BorderingRegionsQuestion(mysql.connection)
        return brq.ask()
    

def register_apis(api):
    """ Registers the API resources defined in this file with the app in it's application factory. """
    
    api.add_resource(Test, '/test/')