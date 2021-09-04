from werkzeug.wrappers import request
from dojos_and_ninjas.config.mysqlconnection import connectToMySQL

class Ninjas:
    def __init__(self,data):
        self.id = data['id']
        self.dojo_id = data['dojo_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def add_ninja(cls, data):
        query = "INSERT INTO ninjas(dojo_id, first_name, last_name, age, created_at, updated_at) VALUES ( (SELECT id AS dojo_id FROM dojos WHERE name = %(dojo_name)s), %(fname)s, %(lname)s, %(age)s, now(), now());"
        print('*** 200 ***', query, data)
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)