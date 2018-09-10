import psycopg2
from Database.database import DatabaseConnection

class Users():
    def __init__(self, user_id, first_name, last_name, email, age, password, created_at):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.password = password
        self.user_id = user_id
        self.created_at = created_at
        self.conn = psycopg2.connect(host="localhost", port="5433", database="Phionamary", user="Phionamary", password="phii100996")

    def create_cursor(self):
        self.cur = self.conn.cursor()
        return self.cur
    
    
    def add_new_user(self):
        new_user = """INSERT INTO Users(first_name, last_name, email, age, password, created_at) 
        VALUES ('{}', '{}', '{}', '{}', '{}', '{}');""".format(self.first_name, self.last_name, 
        self.age, self.email, self.password, self.created_at)
        self.cur.execute(new_user)
        self.conn.commit()
        return True



    def get_user_by_id(self):
        user = """SELECT * FROM users WHERE user_id="{}" """.format(self.user_id)
        self.cur.execute(user)
        single_user = self.cur.fetchone()
        return single_user



    def get_all_user(self):
        users = """SELECT * FROM Users;"""
        self.cur.execute(users)
        all_users = self.cur.fetchall() 
        return all_users 