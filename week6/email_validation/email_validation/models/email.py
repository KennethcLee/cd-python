from email_validation.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Emails:
    def __init__(self, data):
        self.id=data['id']
        self.email=data['email']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails ORDER BY created_at DESC;"
        results = connectToMySQL('email_validation').query_db(query)
        emails = []
        for j in results:
            emails.append(cls(j))
        return emails

    @classmethod
    def add_email(cls, data):
        query = "SELECT * FROM emails WHERE email='HEE1@FAEJ.COM';"
        result = connectToMySQL('email_validation').query_db(query)
        print('*** 420 ***', result, data)
        if connectToMySQL('email_validation').query_db(query):
            flash(f"The email address you entered {data['email']} already exist. Thank you!", 'warning')
            return 'exist'
        else:
            query = "INSERT into emails(email, created_at, updated_at) VALUES (%(email)s, now(), now());"
            print('*** 420B ***', query)
            return connectToMySQL('email_validation').query_db(query, data)

    @staticmethod
    def validate_email(email):
        is_valid = True
        if not EMAIL_REGEX.match(email['email']):
            flash("Invalid email address")
            is_valid = False
        flash(f"The email address you entered {email['email']} is a VALID email address! Thank you!", 'info')
        return is_valid
