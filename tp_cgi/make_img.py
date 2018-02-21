import os
query_string = os.environ["QUERY_STRING"]

print("Content-type:text/html")
print("")
print("<!DOCTYPE html>")
print("<html>")
print("<h1>make_img</h1>")
print("<body>")
print("<form action ='image.py' method='get'>")
print("<label>Size : </label>")
print("<input id='size' name='size' type='number'/>")
print("<input id='valide' type='submit'/>")
print("</div>")
print("</body>")
print("</html>")
