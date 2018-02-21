import os
query_string = os.environ["QUERY_STRING"]

print("Content-type:text/html")
print("")
print("<!DOCTYPE html>")
print("<html>")
print("<h1>hello world</h1>")
print("<a href='index.html'>back to index.html</a>")
print("</html>")
