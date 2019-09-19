import os

from flask import Flask, flash, request, redirect, send_from_directory, url_for
from flask_jwt import JWT, jwt_required
from werkzeug.utils import secure_filename

from file_monkey.auth import get_auth_token, identity
from flask import abort




# Create the app instance
app = Flask(__name__)

# Set the app root and the upload folder
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Set the secret key for session purposes
app.config['SECRET_KEY'] = b'U\xe6\xa8\xc6\xa6K\x7f2\xdf\x1a=\x98p\x8b<e'

# Initialize the JWT extension and set configurations
jwt = JWT(app, get_auth_token, identity)
app.config["JWT_VERIFY_EXPIRATION"] = False     # In a real case it is obviously not recommended not to use expiration of tokens
app.config["JWT_AUTH_HEADER_PREFIX"] = 'Token'

# Set the allowed extensions for the uploaded files
ALLOWED_EXTENSIONS = {'html'}




@app.route('/')
def index():
    return 'yes!'

@app.route('/upload-file/', methods=['POST'])
@jwt_required()
def upload_file():
    """
    Saves a file that is sent by the given file name.
    Restricts the allowed file types to HTML.

    :return (string): Returns if the file was saved successfully
    """

    # Check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        abort(400)
    file = request.files['file']

    # Make sure there is a valid file name
    filename = request.form['name']
    if filename == '':
        flash('Not a valid file name')
        abort(400)
    file.filename = filename

    # Make sure the file has the allowed extension
    if not _allowed_file(filename):
        flash('Not a valid file extension')
        abort(400)

    # Make sure the file is secure - user input should not be trusted
    filename = secure_filename(file.filename)

    # If all the validations passed, save the file
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    # Return OK if successful
    return 'File saved successfully'


@app.route("/browse/<filename>/")
def browse(filename):
    """
    Returns the file that is requested

    :return (file): Returns the requested file
    """

    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


def _allowed_file(filename):
    """
    Helper function that checks if the file has the supported file extension

    :param filename: The filename of which to check the extension

    :return (boolean): If the file has an allowed extension returns True, otherwise False
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
