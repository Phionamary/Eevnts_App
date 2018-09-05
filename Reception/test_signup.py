import unittest
from .signup import Register

class SignUpTest(unittest.TestCase):

    def setUp(self):
        self.register = Register()
        self.a = len(self.register.guest_details)

    def tearDown(self):
        pass
    
    def test_create_new_guest(self):
       self.assertIsInstance(self.register, Register)

    def test_guestName_exists(self):
        self.register.guestName("John Doe")
        self.assertEqual(len(self.register.guest_details), self.a+1)

    def test_guestEmail_exists(self):
        self.register.guestEmails("johndoe@example.com")
        self.assertEqual(len(self.register.guest_details), self.a+1)


    def test_whitespace(self):
        self.register.guestName("")
        self.register.guestName("")
        self.register.guestName("")
        self.assertEqual(len(self.register.guest_details), self.a)

    def test_length_of_guest_list(self):
        y = len(self.register.REGISTER)
        self.register.guestName("John Doe")
        self.register.guestEmails("johndoe@example.com")
        self.register.confirm_guest()
        self.assertEqual(len(self.register.REGISTER), y+1)

    def test_confirm_guest(self):
        self.register.guestName("")
        self.register.guestEmails("")
        self.register.confirm_guest()
        self.assertEqual(len(self.register.REGISTER), 0)


    if __name__=='__main__':
        unittest.main()





