

import os

from flask import Flask, url_for, jsonify
from flask.ext.mysqldb import MySQL
from thanatos.questions import question_utils

app = Flask(__name__)
app.config.update(
    MYSQL_HOST=os.environ.get('MYSQL_HOST', '127.0.0.1'),
    MYSQL_USER=os.environ.get('MYSQL_USER', 'vagrant'),
    MYSQL_PASSWORD=os.environ.get('MYSQL_PASSWORD', 'vagrant'),
    MYSQL_DB=os.environ.get('MYSQL_DB', 'thanatos'),
)

mysql = MySQL(app)

@app.route('/')
def root():
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
                    'single_question',
                    question=question
                )

    return jsonify(data)

@app.route('/questions/random/')
def random_question():
    question_class = question_utils.get_random_question()
    question_instance = question_class(mysql.connection)
    data = question_instance.ask()

    return jsonify(data)

@app.route('/questions/<string:question>/')
def single_question(question):
    question_class = question_utils.get_question(question)
    question_instance = question_class(mysql.connection)
    data = question_instance.ask()

    return jsonify(data)

@app.route('/questions/category/<string:category>/')
def category_question(category):
    question_class = question_utils.get_question_from_category(category)
    question_instance = question_class(mysql.connection)
    data = question_instance.ask()

    return jsonify(data)

@app.route('/questions/category/<string:category>/<string:sub_category>/')
def sub_category_question(category, sub_category):
    question_class = question_utils.get_question_from_sub_category(category, sub_category)
    question_instance = question_class(mysql.connection)
    data = question_instance.ask()

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
