from flask import redirect, render_template, request, session, url_for
from dojos_and_ninjas import app
from dojos_and_ninjas.models.dojo import Dojos
from dojos_and_ninjas.models.ninja import Ninjas

@app.route("/")
def index():
    dojos = Dojos.get_all()
    return render_template("index.html", dojos=dojos)

@app.route("/add_dojo", methods=["POST"])
def add_dojo():
    print('***  1  ***')
    if request.form["dojo_name"] != "":
        data = {
            "dojo_name": request.form["dojo_name"]
        }
        print('***  1  ***', data)
        Dojos.add_dojo(data)
    return redirect("/")

@app.route("/new_ninja")
def new_ninja():
    dojos = Dojos.get_all()
    print('***  2  ***', dojos)
    return render_template("ninjas.html", dojos=dojos)

@app.route("/dojos/<int:id>")
def get_dojo(id):
    data = {
        "id": id
    }
    print('***  3  ***', data)
    dojos = Dojos.get_dojo(data)
    # print('***  3A  ***', data, dojos[0]['name'])
    return render_template("dojos.html", dojos=dojos)
    # return render_template("dojos.html")


@app.route("/add_ninja", methods=['POST'])
def add_ninja():
    data = {
        "dojo_name": request.form["dojo_name"],
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "age": request.form["age"]
    }
    print('***  5  ***', data)
    Ninjas.add_ninja(data)
    return redirect("/")