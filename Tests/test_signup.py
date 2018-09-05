import unittest
from .signup import Register

class SignUpTest(unittest.TestCase):

    def setUp(self):
        self.register = Register()
        self.a = len(self.register.user_details)

    def tearDown(self):
        pass
    
    def test_create_new_user(self):
       self.assertIsInstance(self.register, Register)

    def test_userName_exists(self):
        self.register.userName("John Doe")
        self.assertEqual(len(self.register.user_details), self.a+1)

    def test_userEmail_exists(self):
        self.register.userEmails("johndoe@example.com")
        self.assertEqual(len(self.register.user_details), self.a+1)


    def test_whitespace(self):
        self.register.userName("")
        self.register.userName("")
        self.register.userName("")
        self.assertEqual(len(self.register.user_details), self.a)

    def test_length_of_user_list(self):
        y = len(self.register.REGISTER)
        self.register.userName("John Doe")
        self.register.userEmails("johndoe@example.com")
        self.register.confirm_user()
        self.assertEqual(len(self.register.REGISTER), y+1)

    def test_confirm_user(self):
        self.register.userName("")
        self.register.userEmails("")
        self.register.confirm_user()
        self.assertEqual(len(self.register.REGISTER), 0)


    if __name__=='__main__':
        unittest.main()





