from flask import redirect, render_template, request, session, url_for
from flask.templating import render_template_string
from dojos_and_ninjas import app

@app.route('/')
def index():
    return render_template("/index.html")
