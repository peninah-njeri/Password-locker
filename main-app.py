from user import User
from credentials import Credentials


def create_user(first_name, last_name, password):
    new_user = User(first_name, last_name, password)
    User.save_user(new_user)


def login(username, password):
    """
    This method takes in a username and password, first it checks the existence of that user
     then authenticates based on the password inputed.
    """
    user = User.find_user(username)
    if user is None:
        return False, None
    else:
        is_valid = User.authenticate_user(user, password)
        return is_valid, user


def create_credential(account, username, password):
    new_credential = Credentials(account, username, password)

    Credentials.save_credential(new_credential)


def get_all_credentials():
    return Credentials.credentials_list


def delete_credential(account):
    return Credentials.delete_credential(account)


def main():
    """
    This function is the main entry point to the app and it calls other functions
    as the user interacts with the app
    :return:
    """
    print("""
    
                        Welcome to password locker!             
New? Create an account to get started!

Use the following commands to navigate:
    ca - Create Account 
    li - Log In(Already have an account)
    ex - Exit
-----------------------------------------------------------------------
    """)
    while True:
        print("""
        
        Waiting for your input....
        
        """)
        command = input('>> ').strip()
        if command == 'ca':
            first_name = input('First name >> ')
            last_name = input('Last name >> ')
            password = input('password >> ')

            create_user(first_name, last_name, password)
            print("""
            
        Account successfully created!, Use your first name as the  username to login
            
            """)
        elif command == 'li':
            username = input('username >> ')
            password = input('password >> ')

            is_valid, user = login(username, password)
            if is_valid:
                print(f"""
                                        Welcome {user.first_name.title()}
                """)
                while is_valid:
                    # print("type help to display a list of commands \n")
                    print("""
            ---------------------------------------------------------------------------------
                                    use the following commands to navigate:
              dc - display credentials, cc - create credentials, del - delete a credential, exit - logOut
            ----------------------------------------------------------------------------------            
                    """)
                    command = input('>> ').strip()
                    if command == 'dc':
                        credentials = get_all_credentials()
                        if len(credentials) > 0:
                            for credential in credentials:
                                print(f"platform: {credential.platform} ** username: {credential.username} ** password: {credential.password}")
                        else:
                            print("""
                            
                            You seem to have no saved passwords at the moment
                            
                            """)
                    elif command == 'cc':
                        platform = input('Platform eg.facebook, twitter, dropbox >> ')
                        username = input('username >> ')
                        is_generated = input("Do you want a system generated password?(y/n) >> ")
                        if is_generated == 'y':
                            password = Credentials.generate_random_password()
                        else:
                            password = input('Password >> ')
                        create_credential(platform, username, password)
                        print(f"{platform} credentials successfully saved")
                    elif command == 'del':
                        print('Enter the name of the platform you want to delete')
                        name = input('platform >> ').strip()
                        confirm = input(f"Are you sure you want to delete {name}?(y/n) >> ").strip()
                        if confirm == 'y':
                            is_deleted = delete_credential(name)
                            if is_deleted:
                                print(f"\n {name} credential was successfully deleted")
                            else:
                                print(f"\n {name} credentials do no exist!")
                    elif command == 'exit':
                        break
                    else:
                        print("Sorry i don't understand that command")
            else:
                print("""
                ---------------------------------------
                Invalid username or password, try again
                ---------------------------------------
                """)

        elif command == 'ex':
            break
        else:
            print("Sorry i don't understand that command")


if __name__ == '__main__':
    main()
