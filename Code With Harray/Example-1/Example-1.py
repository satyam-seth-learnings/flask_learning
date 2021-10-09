from flask import Flask
app=Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
@app.route("/Satyam")
def Satyam():
    return "Hello Satyam Bhai"

app.run(debug=True)