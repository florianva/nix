import sys,os
query_string = os.environ["QUERY_STRING"]

print("Content-type:text/html")
print("")
print("<!DOCTYPE html>")
print("<html>")
print("<h1>hello "+query_string+"</h1>")
print("<br>")
print("<a href='index.html'>back to index.html</a>")
print("</html>")
