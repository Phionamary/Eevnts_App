class Register():

    user_details = {}

    REGISTER = []


    def userName(self, user_name):
        if user_name == "":
            print ("Please enter a user\'s name:")
        else:
            self.user_details["user_name"] = user_name

    def userEmails(self, user_email):
        if user_email == "":
            print ("Please enter valid email address:")
        else:
            self.user_details["user_email"] = user_email

    def readFiles(self):
        user_list = []
        with open("users.txt", "r") as current_users_list:
            self.users_list = current_users_list.readlines()
            current_users_list.close()

        return user_list

    def write_to_list(self):
        if self.user_details:
            with open("user.txt") as editted_user_list:
                editted_user_list.write(str(self.user_details) + "\n")
                editted_user_list.close()


    def print_user_list(self):
        with open("user.txt", "r") as updated_list:
            self.user_list = updated_list.readlines()
            print(" These are the invited users: ")

            for name in self.user_list:
                print(name.strip("\n"))
            updated_list.close()

    def confirm_user(self):
        if len(self.user_details) !=  0:
            self.REGISTER.append(self.user_details)
            print ("User confirmed")
            print ("There are " + str(len(self.REGISTER)) + "users on the list")
        else:
            print ("Error in registration")

        

