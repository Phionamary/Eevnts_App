import unittest
from signup import SignUp

class SignUpTest(unittest.TestCase):
    def setUp(self):
        self.signup=SignUp()

    def tearDown(self):
        pass
    
    def test_signup_creation(self):
       self.assertIsInstance(self.signup, SignUp)

    def test_add_user(self):
        self.signup.add("John Doe", "mypass123")
        self.assertEqual(len(self.signup.user_bio),1)

    def test_return_password(self):
        self.signup.add("John","12345")
        self.assertEqual(self.signup.get_password("John"),"12345")

    def test_missing_key(self):
        with self.assertRaises(KeyError):
            self.signup.get_password("John")

    def test_check_length_bio_info(self):
        self.signup.add("John","12345")
        self.signup.add("Sarah","12345")
        self.assertEqual(self.signup.get_bio_length(self.signup.user_bio),2)

    @unittest.skip("WIP")
    def test_unknown_method(self):
        self.assertEqual(self.signup.some_method(),1)

    if __name__=='__main__':
        unittest.main()

