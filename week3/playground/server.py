from flask import Flask, render_template

#material-ui

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/play/')
def play():
    return render_template("play.html", times=3, color="blue")

@app.route('/play/<int:times>/')
def playtimes(times):
    return render_template("play.html", times=times, color="blue")

@app.route('/play/<int:times>/<string:color>')
def playtimescolor(times, color):
    return render_template("play.html", times=times, color=color)

if __name__ == "__main__":
    app.run(debug=True, port=8090)