from os import stat
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app.models.login import Logins
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Recipes:
    def __init__(self, data):
        self.id=data['id']
        self.user_id=data['user_id']
        self.name=data['name']
        self.description=data['description']
        self.instruction=data['instruction']
        self.date_made=data['date_made']
        self.under30mins=data['under30mins']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def get_all(cls, data):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id"
        results = connectToMySQL('recipes').query_db(query, data)
        recipes = []
        print("***  2000A  ***", results)
        print("***  2000B  ***", recipes)
        if results:
            for j in results:
                recipes.append( cls(j))
        return recipes

    @classmethod
    def get_recipe(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s"
        results = connectToMySQL('recipes').query_db(query,data)
        return cls(results[0])

    @classmethod
    def recipe_create(cls, data):
        query = "INSERT INTO recipes(user_id, name, under30mins, description, instruction, date_made, created_at, updated_at) VALUES (%(user_id)s, %(name)s, %(under30mins)s, %(description)s, %(instruction)s, %(date_made)s, now(), now());"
        return connectToMySQL('recipes').query_db(query, data)

    @classmethod
    def recipe_update(cls, data):
        print("***  2010A  ***", data)
        query = "UPDATE recipes SET user_id = %(user_id)s, name = %(name)s, under30mins = %(under30mins)s, description = %(description)s, instruction = %(instruction)s, date_made = %(date_made)s, updated_at = now() WHERE id = %(id)s;"
        return connectToMySQL('recipes').query_db(query, data)

    @classmethod
    def recipe_delete(cls, data):
        print("***  2010A  ***", data)
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL('recipes').query_db(query, data)

    @staticmethod
    def validate_recipe(data):
        is_valid = True
        if len(data['name']) < 1:
            flash("Please enter a recipe name")
            is_valid = False
        if len(data['description']) < 1:
            flash("Please enter a description")
            is_valid = False
        if len(data['instruction']) < 1:
            flash("Please enter instruction")
            is_valid = False
        if (data['date_made'] == ''):
            flash("Please enter a date")
            is_valid = False
        return is_valid

    @staticmethod
    def recipe_exist(data):
        query = "SELECT * FROM recipes WHERE name = %(name)s"
        return connectToMySQL('recipes').query_db(query, data)

# class Recipes:
#     def __init__(self, data):
#         self.id=data['id']
#         self.user_id=data['user_id']
#         self.name=data['name']
#         self.description=data['description']
#         self.instruction=data['instruction']
#         self.date_made=data['date_made']
#         self.under30mins=data['under30mins']
#         self.created_at=data['created_at']
#         self.updated_at=data['updated_at']
#         self.user=None

#     @classmethod
#     def get_all(cls, data):
#         query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id"
#         results = connectToMySQL('recipes').query_db(query,data)
#         recipes = []
#         print("***  2000A  ***", results)
#         print("***  2000B  ***", recipes)
#         if results:
#             for j in results:
#                 data = {
#                     'id': j['user_id'],
#                     'fname': j['first_name'],
#                     'lname': j['last_name'],
#                     'email': j['email'],
#                     'password': j['password'],
#                     'created_at': j['created_at'],
#                     'updated_at': j['updated_at']
#                 }
#                 recipe = cls(j)
#                 recipe.user = Logins(data)
#                 recipes.append(recipe)
#         return recipes

#      recipes[j].user.lname