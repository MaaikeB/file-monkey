
# File Monkey

This is a simple file saver application.
Files can be uploaded and later retrieved by the application.

There are two endpoints:       
- `/upload-file/` - Can be used to upload a file with a specified file name and optional authorization code
- `/browse/<file-name>` - Can be used to retrieve the file


## Example

First authenticate as a user and get an authentication token
```
curl -XPOST localhost:5000/auth --header "Content-Type: application/json" --request POST --data '{"username":"monkey1","password":"abcxyz"}'
```
Response
```
{"access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1Njg4MTc4ODksImlhdCI6MTU2ODgxNzU4OSwibmJmIjoxNTY4ODE3NTg5LCJpZGVudGl0eSI6MX0.8F4CJHvlVKR5d3Sov7M03SM4h96nSYQWpe2fFkQv1FY"}
```

Use that token to upload a file
```
$ echo '<h1>Hi there!</h1>' > test.html
$ curl -XPOST localhost:5000/upload-file/ -F file=@./test.html -F name=myfile.html -H "Authorization: Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1Njg4MTc4ODksImlhdCI6MTU2ODgxNzU4OSwibmJmIjoxNTY4ODE3NTg5LCJpZGVudGl0eSI6MX0.8F4CJHvlVKR5d3Sov7M03SM4h96nSYQWpe2fFkQv1FY"
```
Response:
```
File saved successfully
```

Now browse the file
```
$ curl -v localhost:5000/browse/myfile.html/
```
Response:
```
# [... request headers etc ...]
< HTTP/1.0 200 OK
< Content-Type: text/html; charset=utf-8
< Content-Length: 18
# [... other headers ...]
<h1>Hi there!</h1>
```


## Local Development

You need to have Python3 and pip installed.

Install the requirements (preferrably in a virual environment)
```
pip install requirements
```

Run the app
```
env FLASK_APP=file_monkey.main.py flask run
```
