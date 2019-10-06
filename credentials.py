import random
import string


class Credentials:
    """
    This class is for creating,searching, deleting user credentials and generating passwords 
    """  
     credentials_list = []

    
    def __init__(self, account, username, password):
        self.account = acccount
        self.username = username
        self.password = password

    @classmethod
    def save_credential(cls, credential):
        cls.credentials_list.append(credential)


    @classmethod
    def find_credential(cls, platform):
        for credential in cls.credentials_list:
            if credential.account == account:
                return credential
            else:
                return None
    
    @classmethod
    def get_all_credentials(cls):
        return cls.credentials_list
    
    @staticmethod
    def generate_random_password(password_length=6):
        """
        Create a random passwor in both lowercase and uppercase letters
        """
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(password_length))