class Person(object):

    def __init__(self, personName, age, race, gender):
        
        self.personName = personName
        self.age = age
        self.race = race
        self.gender = gender

    def description(self):
        return "This Person is an {} age year old {}race {} gender  called {} personName ".format(self.personName,self.age,self.race, self.gender)

class User(Person):

    def __init__(self, personName, age, race, gender, email):
        super().__init__(personName, age, race, gender)
        self.email = email


    USERS = []
      
        
    def add_user(self, user):
        user["userId"] = len(self.USERS) + 1
        self.USERS.append(user)
        return self.USERS

    def get_all_users(self):
        return self.USERS
    
    def find_user_by_id(self, userId):
        
        if(self.user_exists(userId)):
            return self.USERS[userId]
            
        return None
            
    def delete_user(self):
        deleted_user = self.USERS[-1]
        self.USERS.remove(deleted_user)
        return self.USERS
        
    def user_exists(self, userId):
        return self.USERS.__contains__(userId)


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