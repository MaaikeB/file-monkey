import json
import os
import pytest

from tempfile import NamedTemporaryFile

from file_monkey.main import app



@pytest.fixture
def client():
    """
    Pytest fixture called client() that configures the application for testing and initializes a new database:
    """

    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client



### UPLOAD

def test_upload(client):
    """Tests that a file can be uploaded using the /upload-file/ endpoint"""

    # Get the authentication token
    response = client.post('/auth', json={"username":"monkey1","password":"abcxyz"})
    auth_token = json.loads(response.data)['access_token']

    # Create a file
    file = NamedTemporaryFile(delete=False)
    file.write(b'Whatever you feel like!\n')

    response = client.open('/upload-file/',
                     method='POST',
                     headers={'Authorization': 'Token {}'.format(auth_token)},
                     content_type='multipart/form-data',
                     buffered=True,
                     follow_redirects=True,
                     data={'file':file, 'name':'awesomeness.html'})

    # Remove the file
    file.close()
    os.unlink(file.name)

    # Assert that the request was successful and the file was saved
    assert response.status_code == 200
    assert response.data == b'File saved successfully'


def test_upload_without_file(client):
    """Tests that when the /upload-file endpoint is called without a file, it returns an error"""

    # Get the authentication token
    response = client.post('/auth', json={"username":"monkey1","password":"abcxyz"})
    auth_token = json.loads(response.data)['access_token']

    response = client.open('/upload-file/',
                         method='POST',
                         headers={'Authorization': 'Token {}'.format(auth_token)},
                         content_type='multipart/form-data',
                         buffered=True,
                         follow_redirects=True,
                         data={'name':'awesomeness.html'})

    # Assert that the request was successful and the file was saved
    assert response.status_code == 400


def test_upload_without_name(client):
    """Tests that when the /upload endpoint is called without a file name, an error is returned"""

    # Get the authentication token
    response = client.post('/auth', json={"username":"monkey1","password":"abcxyz"})
    auth_token = json.loads(response.data)['access_token']

    # Create a file
    file = NamedTemporaryFile(delete=False)
    file.write(b'Whatever you feel like!\n')

    response = client.open('/upload-file/',
                     method='POST',
                     headers={'Authorization': 'Token {}'.format(auth_token)},
                     content_type='multipart/form-data',
                     buffered=True,
                     follow_redirects=True,
                     data={'file':file})

    # Remove the file
    file.close()
    os.unlink(file.name)

    # Assert that the request was successful and the file was saved
    assert response.status_code == 400


def test_upload_file_with_wrong_extension(client):
    """Tests that a file is uploaded with the wrong extension, an error is returned"""

    # Get the authentication token
    response = client.post('/auth', json={"username":"monkey1","password":"abcxyz"})
    auth_token = json.loads(response.data)['access_token']

    # Create a file
    file = NamedTemporaryFile(delete=False)
    file.write(b'Whatever you feel like!\n')

    response = client.open('/upload-file/',
                     method='POST',
                     headers={'Authorization': 'Token {}'.format(auth_token)},
                     content_type='multipart/form-data',
                     buffered=True,
                     follow_redirects=True,
                     data={'file': file, 'name': 'myfile.nonexistingextension'})

    # Remove the file
    file.close()
    os.unlink(file.name)

    # Assert that the request was successful and the file was saved
    assert response.status_code == 400



### BROWSE

def test_browse(client):
    """Tests that an uploaded file can be retrieved by using the /browse endpoint"""


def test_browse_non_existing_file(client):
    """Tests that when trying the browse a file that was never uploaded, an error was returned"""


### AUTHENTICATION

def test_authentication_token_upload():
    """Tests that when the /upload endpoint was called with a valid authentication token, the upload is successfull"""


def test_wrong_authentication_token_upload():
    """Tests that when the /upload endpoint was called with an invalid authentication token, an 401 error is returned"""