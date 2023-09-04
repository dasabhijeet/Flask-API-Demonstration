# Import necessary libraries

from flask import Flask, jsonify, request, make_response, session
from distutils.log import debug
from fileinput import filename
from flask import *
import os.path
from functools import wraps
from flask_limiter import Limiter,util
from flask_limiter.util import get_remote_address

# other way of doing
#from flask_restful import Resource, Api
#from flask_jwt_extended import JWTManager
#from flask_jwt_extended import JWTManager, jwt_required, create_access_token

import jwt  # install PyJWT only, not JWT (installing both raises an error)
import datetime
from werkzeug.utils import secure_filename


# Miscellaneous

app = Flask(__name__)

save_path = 'static/Upload-DIR/'      # uploaded files directory

global_token = 'init'

#img_filename = 'images.jpeg'

# Rate limiter for flask routes
# flask-limiter
limiter = Limiter(get_remote_address, app=app, default_limits=["10 per minute"])


# ------------------------------------------------------
# JWT Authentication Area

# Add super secret key
app.config['SECRET_KEY'] = "secretkeyman"  # Change this as per your requirement to something secure and complex.

# Decorator function

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')

        if not token:
            return jsonify({'message' : 'Token is missing!'}), 403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], options={"verify_signature": True}, algorithms=["HS256"])   # not mentioning algorithm raises unidentified errors both in encode and decode.
        except:
            return jsonify({'message' : 'Token is invalid!'}), 403

        return f(*args, **kwargs)

    return decorated


# JWT Login Part

# Login page route
@app.route("/")
@limiter.limit('5 per minute',override_defaults = True)   # Rate limiter as needed
def loginpage():
    return render_template('login.html')

# Get login details, jwt encode and redirect url
@app.route('/login', methods=['POST'])
def login():
    """
    Logs a user in by parsing a POST request containing user credentials and
    issuing a JWT token.
    """
    data = request.form
    username = data['username']
    password = data['password']

    if username == 'admin1' and password == 'admin1':
#       token = jwt.encode({'user': data['username'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'], algorithm="HS256")   # minutes
        token = jwt.encode({'user': data['username'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=12)}, app.config['SECRET_KEY'], algorithm="HS256")  # seconds
        global_token = token
#       return jsonify(message="Login Succeeded!", access_token=token), 201
#       return redirect(url_for('protected')+"?token="+token)
        return redirect(url_for('index')+"?token="+global_token)          # this return statement is special, redirects the user to a protected route while adding token to URL, only mention name of def index(): function, not /index route, otherwise error (werkzeug.routing.exceptions.BuildError: Could not build url for endpoint 'index') will occur
    else:
        return jsonify(message="Wrong Username or Password"), 401
    return token

# Set Browser Cookies
# Future Idea :) 

'''
# App authentication test route
@app.route("/protected", methods=["GET"])
@token_required
def protected():
    return "This is protected area"
    #return render_template('index.html')
'''

#-------------------------------------------------------
# Main file upload application section

@app.route('/index')
@token_required
@limiter.limit('5 per minute',override_defaults = True)     # Rate limiter as needed
def index():
    return render_template('index.html')


# Upload verification and redirection with token, currently not working

'''
@app.route('/verify', methods = ['POST'])
def verify():
    if request.method == "POST":
        uploaded_file = request.files['file']
        #filename = uploaded_file.filename
        filename = secure_filename(uploaded_file.filename)

    
        if filename != '':
            #return redirect(url_for('success')+"?token="+global_token)   # global token doesn't return token value and defaults to 'init'
            return jsonify(global_token)

        elif filename == '':
            return redirect(url_for('index')+"?token="+global_token)
            #return "filename isnt there"
'''   
    

# Upload and save section

@app.route('/success', methods = ['POST'])
#@token_required
def success():  
    if request.method == 'POST':  
        fl = request.files['file']
        fl.save(save_path + fl.filename)
        session['uploaded_img_file_path'] = os.path.join(save_path, fl.filename)     # Get uploaded file's filepath
        return render_template("Acknowledge.html", name = fl.filename)



# Render Image

@app.route('/')
@app.route('/render')
def render():
    full_filename = session.get('uploaded_img_file_path', None)
    full_filename = full_filename.replace('static/', '')       # Remove 'static/' string from filename url as it gives error in html static rendering, html defaults to get files from static directory. Disabling this adds two static directories, raising an error.
    return render_template("render.html", user_image = full_filename)     # Pass the filename to HTML's IMG SRC tag for it to render
    #return full_filename


if __name__ == '__main__':
    app.run(debug=True)


# Program last updated: 4 September 2023, 11:05 PM
# Program by: https://www.github.com/dasabhijeet
# Program name: Flask API Demonstration