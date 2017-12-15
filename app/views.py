from flask import render_template
from app import app

#
@app.route('/')
def index():
    '''
    View root page function that returns the index and its data
    '''
    message = "Hello owolr"
    return render_template('index.html', message= message)
@app.route('/user/<int:user_id>')
def user(user_id):
    '''
    View root function that returns a user page and data
    '''
    return render_template('user.html',id = user_id)