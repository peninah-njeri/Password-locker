

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
        