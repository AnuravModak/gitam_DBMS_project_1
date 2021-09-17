from flask import Flask
import codecs
from flask import request
import connector


app=Flask("__name__")
@app.route("/")
def hello_world():
    f = codecs.open("home.html", 'r')

    return f.read()
@app.route("/next")
def hello():
    return "<p>Hello From Server<p>"

@app.route("/method",methods=["POST"])
def method():
    name=request.form.get("name")
    email=request.form.get("email")
    mobile=request.form.get("mobile")
    if mobile is None:
        mobile="NULL"

    password=request.form.get("password")
    print(name,mobile,email,password)
    y=connector.connector(name,email,mobile,password)

    return y+"....name:"+name+" email: "+email+" mobile: "+mobile+" password is hidden"



if __name__ == "__main__":
    app.run(debug=True)
