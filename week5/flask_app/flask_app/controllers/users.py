from flask import redirect, render_template, request, session, url_for
from flask_app import app
from flask_app.models.user import Users

@app.route('/', methods=['GET'])
def index():
    users = Users.get_all()
    print('***  1  ***', users)
    for j in users:
        print('***  1A  ***', j.updated_at)
    return render_template("/index.html", all_users = users)

@app.route('/adduser', methods=['POST'])
def adduser():
    print('***  3  ***')
    return render_template("/adduser.html")

@app.route('/showuser/<int:id>')
def showuser(id):
    print('***  6  ***')
    data = {
        'id': id
    }
    user = Users.get_user(data)
    print('***  6A  ***', user[0]['id'])
    return render_template("/showuser.html", user=user)

@app.route('/edituser/<int:id>')
def edituser(id):
    print('***  5  ***')
    data = {
        'id': id,
    }
    user = Users.get_user(data)
    return render_template("/edituser.html", user=user)

@app.route('/save', methods=['POST'])
def save():
    print('***  7  ***')
    data = {
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email']
    }
    print('***  7A  ***')
    Users.save(data)
    return redirect("/")

@app.route('/edit/<int:id>', methods=['POST'])
def edit(id):
    print('***  8  ***')
    data = {
        'id': id,
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email']
    }
    user=Users.edit(data)
    print('***  8A  ***', data)
    return redirect(url_for('edituser', id=id))

@app.route('/deleteuser/<int:id>')
def delete(id):
    print('***  9  ***')
    data = {
        'id': id
    }
    Users.delete(data)
    print('***  9A  ***', data)
    return redirect(url_for('index'))
