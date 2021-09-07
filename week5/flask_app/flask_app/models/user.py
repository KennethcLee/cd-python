from werkzeug.wrappers import request
from flask_app.config.mysqlconnection import connectToMySQL

class Users:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def get_user(cls, data):
        print('***  11  ***', data)
        query = "SELECT * FROM users WHERE id = %(id)s;"
        print('***  11A  ***', query)
        results = connectToMySQL('user_ca').query_db(query, data)
        print('***  11B  ***', results)
        return results
    @classmethod
    def get_all(cls):
        print('***  13  ***')
        query = "SELECT * FROM users;"
        results = connectToMySQL('user_ca').query_db(query)
        users = []
        print('***  13A  ***', results, results[0]['id'])
        for j in results:
            users.append( cls(j) )
        print('***  13B  ***', users, users[0].last_name)
        return users

    @classmethod
    def save(cls, data):
        print('***  15  ***', data)
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES ( %(fname)s, %(lname)s, %(email)s, now(), now());"
        return connectToMySQL('user_ca').query_db(query, data)

    @classmethod
    def edit(cls, data):
        print('***  17  ***', data)
        query = "UPDATE users SET first_name = %(fname)s, last_name = %(lname)s, email = %(email)s, updated_at = now() WHERE id = %(id)s;"
        print('***  17A  ***', query)
        return connectToMySQL('user_ca').query_db(query, data)

    @classmethod
    def delete(cls, data):
        print('***  19  ***', data)
        query = "DELETE FROM users WHERE id = %(id)s;"
        print('***  19A  ***', query)
        return connectToMySQL('user_ca').query_db(query, data)
