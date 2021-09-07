from flask import redirect, render_template, session, url_for, request
from flask.templating import render_template_string
from email_validation import app
from email_validation.models.email import Emails

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=['POST'])
def submit():
    print('*** 310 ***')
    data = {
        'email': request.form['email']
    }
    if not Emails.validate_email(data):
        print('*** 310A ***', data)
        return redirect("/")
    Emails.add_email(data)
    print('*** 310B ***', data)
    return redirect("/email")

@app.route("/email")
def email():
    print('*** 320 ***')
    emails=Emails.get_all()
    return render_template ("email.html", emails=emails)