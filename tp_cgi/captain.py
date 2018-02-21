import os
query_string = os.environ["QUERY_STRING"]

print("Content-type:text/html")
print("")
print("<!DOCTYPE html>")
print("<html>")
print("<h1>print captain</h1>")
print("<body>")
with open("captain.txt", "r") as ins:
    for line in ins:
        print(line)
        print("<br>")
    
print("</body>")
print("<br>")
print("<a href='index.html'>back to index.html</a>")
print("</html>")
