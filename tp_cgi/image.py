import os, cgi
import utils.py as utils
query_string = os.environ["QUERY_STRING"]
form = cgi.FieldStorage()
size = form.getfirst("size", "")
utils.make_img(size, 'img.png')
print("Content-type:text/html")
print("")
print("<!DOCTYPE html>")
print("<html>")
print("<h1>cgi_field</h1>")
print("<body>")
print("<img src='img.png' alt='Image'>")
print("</body>")
print("<br>")
print("<a href='index.html'>back to index.html</a>")
print("</html>")
