from flask import Flask, render_template, request, redirect, session

app=Flask(__name__)
app.secret_key="Test"

@app.route('/')
def counter():
    if 'count' not in session:
        session['count']=0
    elif 'anynum' not in session:
        session['count']+=1
    if 'visit' not in session:
        session['visit']=0
    else:
        session['visit']+=1
    return render_template('/index.html')

@app.route('/addtwo')
def addtwo():
    if 'count' not in session:
        session['count']=0
    else:
        session['count']+=2
    return render_template('/index.html')

@app.route('/reset')
def reset():
    session.pop('count')
    return redirect('/')

@app.route('/anynum', methods=['POST'])
def anynum():
    session['count']+=(int(request.form['anynum']))
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True, port=8092)