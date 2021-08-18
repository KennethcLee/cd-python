from flask import Flask, render_template, request, redirect, session

app=Flask(__name__)
app.secret_key="Test"

@app.route('/')
def counter():
    if 'count' not in session:
        session['count']=0
    else:
        session['count']+=1
    return render_template('/index.html')

@app.route('/reset')
def reset():
    session['count']=-1
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True, port=8092)