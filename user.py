class User:
    users_list = []
    
    def __init__(self, first_name, last_name, password):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    @classmethod
    def save_user(cls, user):
        cls.users_list.append(user)    






     