from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def checker():
    return render_template("index.html", col=8, row=8, color='red', bcolor='black')

@app.route('/<int:row>/')
def checkerrow(row):
    return render_template("index.html", col=8, row=row, color='red', bcolor='black')

@app.route('/<int:row>/<int:col>')
def checkerrowcol(row, col):
    return render_template("index.html", col=col, row=row, color='red', bcolor='black')

@app.route('/<int:row>/<int:col>/<string:bcolor>')
def checkerrowcolbcolor(row, col, bcolor):
    return render_template("index.html", col=col, row=row, color='red', bcolor=bcolor)

@app.route('/<int:row>/<int:col>/<string:bcolor>/<string:color>')
def checkerrowcolbcolorcolor(row, col, bcolor, color):
    return render_template("index.html", col=col, row=row, color=color, bcolor=bcolor)

if __name__=="__main__":
    app.run(debug=True, port=8090)