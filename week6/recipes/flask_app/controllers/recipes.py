import re
from flask import Flask, request, redirect, render_template, session, url_for, flash
from flask_app.models.login import Logins
from flask_app.models.recipe import Recipes
from flask_app import app
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)
app.secret_key="randomstring"

@app.route("/dashboard")
def dashboard():
    if session.get('logged_in') == True:
        data = {
            'user_id': session['user_id'],
            'email': session['email']
        }
        user=Logins.get_user(data)
        recipes=Recipes.get_all(data)
        # print("*** 1000 ***", user, recipes, recipes[0], recipes[0].id)
        return render_template("/dashboard.html", user=user, recipes=recipes)
    else:
        return redirect("/login")

@app.route("/recipes/new")
def recipes_new():
    if session.get('logged_in') == True:
        return render_template("/new.html")
    else:
        return redirect("/login")

# @app.route("/recipes/new")
# def recipes_new():
#     if session.get('logged_in') == True:
#         data = {
#             'user_id': session['user_id'],
#             'email': session['email']
#         }
#         user=Logins.get_user(data)
#         recipes=Recipes.get_all(data)
#         print("*** 1000 ***", user)
#         return render_template("/new.html", user=user, recipes=recipes)
#     else:
#         return redirect("/login")

@app.route("/recipe_create", methods=['POST'])
def recipe_create():
    print("***  1010A  ***", request.form)
    print("***  1010B  ***", request.form.getlist('fav_language'))
    if session.get('logged_in') == True:
        if not Recipes.validate_recipe(request.form):
            return redirect("/recipes/new")
        data = {
            'user_id': session['user_id'],
            'name': request.form['name'],
            'description': request.form['description'],
            'instruction': request.form['instruction'],
            'date_made': request.form['date_made'],
            'under30mins': request.form['under30mins']
        }
        print("***  1010B  ***", request.form, data)

        if Recipes.recipe_exist(data):
            flash("Recipe name already exists.")
            return redirect("/recipes/new")
        Recipes.recipe_create(data)
        return redirect("/dashboard")
    else:
        return redirect("/login")


@app.route("/recipes/edit/<int:id>")
def recipe_edit_page(id):
    print("***  1020  ***", id)
    if session.get('logged_in') == True:
        data = {
            'id': id
        }
        recipes=Recipes.get_recipe(data)
        print("***  1020A  ***", data, recipes)
        session['recipe_id']=id
        return render_template("/edit.html", recipes=recipes)
    else:
        return redirect("/login")

@app.route("/recipe_edit", methods=['POST'])
def recipe_edit():
    print("***  1030A  ***", request.form, session)
    if session.get('logged_in') == True:
        if not Recipes.validate_recipe(request.form):
            return redirect("/recipes/new")
        data = {
            'id': session['recipe_id'],
            'user_id': session['user_id'],
            'name': request.form['name'],
            'description': request.form['description'],
            'instruction': request.form['instruction'],
            'date_made': request.form['date_made'],
            'under30mins': request.form['under30mins']
        }
        # print("***  1010B  ***", request.form, data)

        Recipes.recipe_update(data)
        session.pop('recipe_id')
        return redirect("/dashboard")
    else:
        return redirect("/login")

@app.route("/recipes/<int:id>")
def recipe_view(id):
    print("***  1040A  ***", request.form, session)
    if session.get('logged_in') == True:
        data = {
            'id': id
        }
        user=Logins.get_user(data)
        recipes=Recipes.get_recipe(data)
        return render_template("/view.html", recipes=recipes, user=user)
    else:
        return redirect("/login")

@app.route("/recipes/delete/<int:id>")
def recipe_delete(id):
    print("***  1030A  ***", request.form, session)
    if session.get('logged_in') == True:
        data = {
            'id': id
        }
        # print("***  1010B  ***", request.form, data)
        Recipes.recipe_delete(data)
        return redirect("/dashboard")
    else:
        return redirect("/login")

    # return render_template(url_for ("/recipes/<int:recipe_id>", recipe_id=recipes.id))