import unittest
from user import user


class TestUserCredentials(unittest.TestCase):

    def setUp(self):
        """
        Set a fake user and credential for each test
        """
        self.test_user = User('ninah', 'njeri', '123')
        User.users_list.append(self.test_user)

      
    def test_create_user(self):
        new_contact = User('pesh', 'nje', '0000')
        self.assertEqual(new_contact.first_name, 'pesh')
        self.assertEqual(new_contact.last_name, 'nje')
        self.assertEqual(new_contact.password, '0000')

    def test_save_user(self):
        User.save_user(self.test_user)
        has_user = self.test_user in User.users_list
        self.assertTrue(has_user)    

