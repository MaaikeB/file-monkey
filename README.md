
# File Monkey

This is a simple file saver application.
Files can be uploaded and later retrieved by the application.

There are two endpoints:       
- `/upload-file/` - Can be used to upload a file with a specified file name and optional authorization code
- `/browse/<file-name>` - Can be used to retrieve the file


## Endpoints

#### File Upload

#### Browse



## Example

```
$ echo '<h1>Hi there!</h1>' > test.html
$ curl -XPOST localhost:8000/upload-file/ \
    -F file=@./test.html \
    -F name=myfile.html \
    -H "Authorization: Token 1234567890abcd"
OK
$ curl -v localhost:8000/browse/myfile.html/
# [... request headers etc ...]
< HTTP/1.0 200 OK
< Content-Type: text/html; charset=utf-8
< Content-Length: 18
# [... other headers ...]
<h1>Hi there!</h1>
```