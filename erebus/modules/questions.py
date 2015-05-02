

from flask.ext.restful import Resource

from erebus.extensions import mysql
from thanatos.questions import question_utils


class RandomQuestion(Resource):
    """  """
    
    def get(self):
        question_class = question_utils.get_random_question()
        question_instance = question_class(mysql.connection)
        question = question_instance.ask()
        
        return question

class Question(Resource):
    """  """
    
    def get(self, question):
        question_class = question_utils.get_question(question)
        question_instance = question_class(mysql.connection)
        question = question_instance.ask()
        
        return question


class CategoryQuestion(Resource):
    """  """
    
    def get(self, category):
        question_class = question_utils.get_question_from_category(category)
        question_instance = question_class(mysql.connection)
        question = question_instance.ask()
        
        return question


class SubCategoryQuestion(Resource):
    """  """
    
    def get(self, category, sub_category):
        question_class = question_utils.get_question_from_sub_category(category, sub_category)
        question_instance = question_class(mysql.connection)
        question = question_instance.ask()
        
        return question
    

def register_apis(api):
    """ Registers the API resources defined in this file with the app in it's application factory. """
    
    api.add_resource(
        RandomQuestion(),
        '/questions/random/',
        endpoint='random_question'
    )
    
    api.add_resource(
        Question(),
        '/questions/<string:question>/',
        endpoint='question'
    )
    
    api.add_resource(
        CategoryQuestion(),
        '/questions/category/<string:category>/',
        endpoint='category_question'
    )
    
    api.add_resource(
        SubCategoryQuestion(),
        '/questions/category/<string:category>/<string:sub_category>/',
        endpoint='sub_category_question'
    )