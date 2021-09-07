from werkzeug.wrappers import request
from dojos_and_ninjas.config.mysqlconnection import connectToMySQL

class Dojos:
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos ORDER BY name;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        print('*** 100 ***', results, results[0]['id'])
        return results

    @classmethod
    def add_dojo(cls, data):
        print('*** 104 ***', data, id)
        query = "INSERT INTO dojos(name, created_at, updated_at) VALUES ( %(dojo_name)s, now(), now());"
        print('*** 104 ***', query)
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)

    @classmethod
    def get_dojo(cls, data):
        print('*** 105 ***', data, id)
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        print('*** 105A ***', query, data, results)
        return results
