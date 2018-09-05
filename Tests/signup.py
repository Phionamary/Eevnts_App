class Register():

    guest_details = {}

    REGISTER = []


    def guestName(self, guest_name):
        if guest_name == "":
            print ("Please enter a guest\'s name:")
        else:
            self.guest_details["guest_name"] = guest_name

    def guestEmails(self, guest_email):
        if guest_email == "":
            print ("Please enter valid email address:")
        else:
            self.guest_details["guest_email"] = guest_email

    def readFiles(self):
        guest_list = []
        with open("guests.txt", "r") as current_guest_list:
            self.guest_list = current_guest_list.readlines()
            current_guest_list.close()

        return guest_list

    def write_to_list(self):
        if self.guest_details:
            with open("guest.txt") as editted_guest_list:
                editted_guest_list.write(str(self.guest_details) + "\n")
                editted_guest_list.close()


    def print_guest_list(self):
        with open("guest.txt", "r") as updated_list:
            self.guest_list = updated_list.readlines()
            print(" These are the invited guests: ")

            for name in self.guest_list:
                print(name.strip("\n"))
            updated_list.close()

    def confirm_guest(self):
        if len(self.guest_details) !=  0:
            self.REGISTER.append(self.guest_details)
            print ("Guest confirmed")
            print ("There are " + str(len(self.REGISTER)) + "guests on the list")
        else:
            print ("Error in registration")

        

