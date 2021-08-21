from flask import Flask, render_template, redirect, request, session

app=Flask(__name__)
app.secret_key="Dojo Survey"

@app.route('/')
def survey():
    return render_template('/index.html')

@app.route('/process', methods=['POST'])
def process():
    session['name']=request.form['name']
    session['location']=request.form['location']
    session['language']=request.form['language']
    session['comment']=request.form['comment']
    session['learned']=request.form.getlist('learned')
    session['graduated']=request.form['graduated']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('/result.html')

@app.route('/clear', methods=['POST'])
def clear():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True, port=5000)
