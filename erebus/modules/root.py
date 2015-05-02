

from flask import url_for
from flask.ext.restful import Resource

from thanatos.questions import question_utils

class Root(Resource):
    """  """
    
    def get(self):
        question_details = question_utils.get_all_question_details()
        
        data = {
            'random_question': url_for('random_question'),
            'categories': question_utils.get_all_question_details(),
        }
        
        for category in data['categories']:
            data['categories'][category]['random_category_question'] = url_for('category_question', category=category)
            
            for sub_category in data['categories'][category]['sub_categories']:
                data['categories'][category]['sub_categories'][sub_category]['random_category_question'] = url_for(
                    'sub_category_question',
                    category=category,
                    sub_category=sub_category
                )
            
                for question in data['categories'][category]['sub_categories'][sub_category]['questions']:
                    data['categories'][category]['sub_categories'][sub_category]['questions'][question]['href'] = url_for(
                        'question',
                        question=question
                    )
        
        return data


def register_apis(api):
    """ Registers the API resources defined in this file with the app in it's application factory. """
    
    api.add_resource(
        Root,
        '/',
        endpoint='root'
    )