users = []

class Users(object):

    def __init__(self,userId, userName, userEmail):
        self.userId = userId
        self.userName = userName
        self.userEmail = userEmail

    def to_json(self):
        return{'userId': self.userId,'userName': self.userName,'userEmail': self.userEmail}

    
user1 = Users(1, "Phiona Mary Kigai", "phionamarykigai@example.com")
users.append(user1.to_json())


user2 = Users(2, "John Doe", "johndoe@example.com")
users.append(user2.to_json())

user3 = Users(3, "Sarah Smith", "sarahsmith@example.com")
users.append(user3.to_json())