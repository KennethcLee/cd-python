import re
from flask import Flask, render_template, request, redirect, session
import random

app=Flask(__name__)
app.secret_key="Game Info"

@app.route('/')
def game():
    if 'value' not in session:
        session['value']=random.randrange(1,100)
    if 'count' not in session:
        session['count']=0
    print(session['value'])
    return render_template('/index.html')

@app.route('/guess', methods=['GET', 'POST'])
def guess():
    # if request.method=='POST':
    #     pass
    if request.form['guess']:
        session['guess']=(int(request.form['guess']))
        print(session['guess'])
    session['count']+=1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    if 'guess' in session:
        session.pop('guess')
    if 'value' in session:
        session.pop('value')
    if 'count' in session:
        session.pop('count')
    print(session)
    return redirect('/')

@app.route('/leader', methods=['POST'])
def leader():
    if 'leader' not in session:
        session['leader'] = [[session['count'], request.form['name']]]
    else:
        leaderBoard=session['leader']
        for j in range(len(leaderBoard)):
            if leaderBoard[j][0] > session['count']:
                leaderBoard.insert(j-1, [session['count'], request.form['name']])
        if j == len(leaderBoard) - 1:
            leaderBoard.append([session['count'], request.form['name']])
        session['leader']=leaderBoard
    return redirect('/leaderboard')

@app.route('/leaderboard')
def leaderboard():
    return render_template('/leader.html')

@app.route('/resetleader', methods=['POST'])
def resetleader():
    if 'leader' in session:
        session.pop('leader')
    return redirect('/leaderboard')

if __name__=="__main__":
    app.run(debug=True, port=8094)