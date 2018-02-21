import sys,os
query_string = os.environ["QUERY_STRING"]

print("Content-type:text/html")
print("")
print("<!DOCTYPE html>")
print("<html>")
print("<h1>print envs</h1>")
print("<body>")
for name, value in os.environ.items():
    print (name+"\t= "+value+"<br/>")
print("</body>")
print("<br>")
print("<a href='index.html'>back to index.html</a>")
print("</html>")
