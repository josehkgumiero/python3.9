# A Minimal Application
##################################################

from flask import Flask

app = Flask(__name__)

@app.route("""/""")
def _hello_world():
    return "<p>Hello, World!</p>"

# HTML Escaping
##################################################

from markupsafe import escape

#@app.route("""/<_name>""")
#def _hello_name(_name):
#    return "<p>Hello, {0}!</p>".format(_name)

# Routing
##################################################

@app.route('/index')
def index():
    return 'Index Page'

#@app.route('/hello')
#def hello():
#    return 'Hello, World'

# Variables Rules
##################################################

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

# Unique URLs / Redirection Behavior
##################################################

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

# URL Building
##################################################

from flask import url_for

#@app.route('/login')
#def login():
#    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
#    print(url_for('login'))
#    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

# HTTP Methods
##################################################

from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'do_the_login()'
    else:
        return 'show_the_login_form()'

# Rendering Templates
##################################################
    
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

# Context Locals
##################################################

from flask import request

with app.test_request_context('/test_post', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'GET'

# The Request Object
##################################################
#
#from flask import request
#
#@app.route('/login', methods=['POST', 'GET'])
#def login():
#    error = None
#    if request.method == 'POST':
#        if valid_login(request.form['username'],
#                       request.form['password']):
#            return log_the_user_in(request.form['username'])
#        else:
#            error = 'Invalid username/password'
#    # the code below is executed if the request method
#    # was GET or the credentials were invalid
#    return render_template('login.html', error=error)

# File Uploads
##################################################
#
#from flask import request
#
#@app.route('/upload', methods=['GET', 'POST'])
#def upload_file():
#    if request.method == 'POST':
#        f = request.files['the_file']
#        f.save('/var/www/uploads/uploaded_file.txt')

# Cookies
##################################################
#
## Reading cookies
#
#from flask import request
#
#@app.route('/')
#def index():
#    username = request.cookies.get('username')
#    # use cookies.get(key) instead of cookies[key] to not get a
#    # KeyError if the cookie is missing.
#
## Storing cookies
#
#from flask import make_response
#
#@app.route('/')
#def index():
#    resp = make_response(render_template(...))
#    resp.set_cookie('username', 'the username')
#    return resp

# Redirects
##################################################
#
#from flask import abort, redirect, url_for
#
#@app.route('/')
#def index():
#    return redirect(url_for('login'))
#
#@app.route('/login')
#def login():
#    abort(401)
#    this_is_never_executed()

# Errors
##################################################
#
#from flask import render_template
#
#@app.errorhandler(404)
#def page_not_found(error):
#    return render_template('page_not_found.html'), 404

# About Responses
##################################################
#
#from flask import make_response
#
#@app.errorhandler(404)
#def not_found(error):
#    resp = make_response(render_template('error.html'), 404)
#    resp.headers['X-Something'] = 'A value'
#    return resp

# APIs with JSON
##################################################
#
#@app.route("/me")
#def me_api():
#    user = get_current_user()
#    return {
#        "username": user.username,
#        "theme": user.theme,
#        "image": url_for("user_image", filename=user.image),
#    }
#
#@app.route("/users")
#def users_api():
#    users = get_all_users()
#    return [user.to_json() for user in users]

# Sessions
##################################################
#
#from flask import session
#
## Set the secret key to some random bytes. Keep this really secret!
#app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
#
#@app.route('/')
#def index():
#    if 'username' in session:
#        return f'Logged in as {session["username"]}'
#    return 'You are not logged in'
#
#@app.route('/login', methods=['GET', 'POST'])
#def login():
#    if request.method == 'POST':
#        session['username'] = request.form['username']
#        return redirect(url_for('index'))
#    return '''
#        <form method="post">
#            <p><input type=text name=username>
#            <p><input type=submit value=Login>
#        </form>
#    '''
#
#@app.route('/logout')
#def logout():
#    # remove the username from the session if it's there
#    session.pop('username', None)
#    return redirect(url_for('index'))

# How to generate good secret keys
##################################################

# Message Flashing
##################################################

# Logging
##################################################

# Hooking in WSGI Middleware
##################################################

# Using Flask Extensions
##################################################

# Deploying to a Web Server
##################################################