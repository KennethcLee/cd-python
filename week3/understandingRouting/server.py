from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", phrase="hello", times=5)

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:name>')
def say(name):
    return "Hi " + name + "!"

@app.route('/repeat/<int:times>/<string:name>')
def repeat(times, name):
    return f"{name * times}"

@app.route('/', defaults={'path': ''})
@app.route('/<path:p>')
def catch_all(p):
    return "Sorry! No reponse.  Try again."

if __name__=="__main__":
    app.run(debug=True, port=8090)
