from flask import Flask,render_template
app=Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/bootstrap")
def about():
    return render_template('bootstrap.html')

app.run(debug=True)