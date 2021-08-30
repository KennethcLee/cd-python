from flask import Flask, redirect, render_template, request, session
from user import Users

app=Flask(__name__)

@app.route('/')
def index():
    users = Users.get_all()
    print('***  6  ***', users)
    for j in users:
        print('***  6A  ***', j.updated_at)
    return render_template("/index.html", all_users = users)

@app.route('/adduser', methods=['POST'])
def adduser():
    print('***  5  ***')
    return render_template("/adduser.html")

@app.route('/save', methods=['POST'])
def save():
    print('***  1  ***')
    data = {
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email']
    }
    print('***  2  ***')
    Users.save(data)
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)
