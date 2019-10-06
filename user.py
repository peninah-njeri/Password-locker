class User:
    users_list = []
    
    def __init__(self, first_name, last_name, password):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    @classmethod
    def save_user(cls, user):
        cls.users_list.append(user)

    
    @classmethod
    def find_user(cls, username):
        for user in cls.users_list:
            if user.first_name == username:
                return user
            else:
                return None


    @classmethod
    def validate_user(cls, user, password):
        """
        Takes in a user and a password and verifies that the password provided is equal to the users password
        :param user:
        :param password:
        :return: boolean
        """
        if user.password == password:
            return True
        else:
            return False
            



     