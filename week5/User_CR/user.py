from mysqlconnection import connectToMySQL

class Users:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def get_all(cls):
        print('***  3  ***')
        query = "SELECT * FROM users;"
        results = connectToMySQL('user_ca').query_db(query)
        users = []
        print('***  3A  ***', users)
        for j in results:
            users.append( cls(j) )
        print('***  3B  ***', users[0].last_name)
        return users
    @classmethod
    def save(cls, data):
        print('***  4  ***')
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES ( %(fname)s, %(lname)s, %(email)s, now(), now());"
        return connectToMySQL('user_ca').query_db(query, data)

