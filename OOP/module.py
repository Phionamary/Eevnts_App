from flask import Flask

app = Flask(__name__)

class Person(object):

    def __init__(self, name, age, race, gender):
        
        self.name = name
        self.age = age
        self.race = race
        self.gender = gender

    def description(self):
        return "This Person is an {} age year old {}race {} gender  called {} name ".format(self.name,self.age,self.race, self.gender)


class User(Person):

    def __init__(self, name, age, race, gender, email):
        super().__init__(name, age, race, gender)
        self.email = email
      
    all_users = []


    def add_user(self, user):
        user["userId"] = len(self.all_users) + 1
        self.all_users.append(user)
        return self.all_users

    def get_all_users(self):
        return self.all_users
    
    def find_user_by_id(self, userId):
        
        if(self.user_exists(userId)):
            return self.all_users[userId]
            
        return None
            
    def delete_user(self):
        deleted_user = self.all_users[-1]
        self.all_users.remove(deleted_user)
        return self.all_users
        
    def user_exists(self, userId):
        return self.all_users.__contains__(userId)


class GuestList():

    guests = []
    
    def add_guest(self, guest_details):
        self.guests.append(guest_details)
        return self.guests

    def get_all_guests(self):
        return self.guests

    def delete_guest(self, guest_id):
        deleted_guest = self.guests[guest_id]
        self.guests.remove(guest_id)
        return deleted_guest

if __name__=='__main__':
    app.run(debug=True)