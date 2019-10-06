import unittest
from user import User



class TestUser(unittest.TestCase):

    def setUp(self):
        """
        Sets a fake user for each test
        """
        self.test_user = User('ninah', 'njeri', '123')
        User.users_list.append(self.test_user)

    def tearDown(self):
        """
        cleans up after each test, removes dummy user and credential
        :return:
        """
        User.users_list.clear()    

      
    def test_create_user(self):
        new_contact = User('pesh', 'nje', '0000')
        self.assertEqual(new_contact.first_name, 'pesh')
        self.assertEqual(new_contact.last_name, 'nje')
        self.assertEqual(new_contact.password, '0000')

    def test_save_user(self):
        User.save_user(self.test_user)
        has_user = self.test_user in User.users_list
        self.assertTrue(has_user)    

    def test_find_user(self):
        user = User.find_user(self.test_user.first_name)
        self.assertEqual(user, self.test_user)

    def test_validate_user(self):
        is_valid = User.validate_user(self.test_user, self.test_user.password)
        self.assertTrue(is_valid)
    

        
