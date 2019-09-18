

### UPLOAD

def test_upload(client):
    """Tests that a file can be uploaded using the /upload endpoint"""


def test_upload_without_file():
    """Tests that when the /upload endpoint is called without a file, it returns an error"""


def test_upload_without_name():
    """Tests that when the /upload endpoint is called without a file name, an error is returned"""


def test_upload_file_with_wrong_extension():
    """Tests that a file is uploaded with the wrong extension, an error is returned"""



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