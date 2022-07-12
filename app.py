from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from markupsafe import escape
from waitress import serve


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False 


# @app.route('/')
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        pass
    else:
        return render_template('index.html')
    # return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/nextpage', methods=['POST','GET'])
def nextpage():
    if request.method == 'POST':
        pass
    else:
        return render_template('nextpage.html')

    # return 'Next Page'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)



if __name__=="__main__":
    serve(app, host='0.0.0.0', port=5001)