#### This is a python application that allows a user to generate and store passwords for various accounts.

## Created By Peninah Njeri
https://github.com/peninah-njeri/password-locker
## Description
Password Locker is a terminal run python application that allows users to store details i.e. usernames and passwords of their various accounts.

## User Stories
These are the behaviours/features that the application implements for use by a user.

As a user I would like:
* To create an account with my details - log in and password
* Store my existing login credentials
* Create a new password for a new account
## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display codes for navigation | **in terminal $./main_app.py** | Welcome and for easy navigation choose an option: ca - Create Account, li - Log In, ex - Exit |
| Display prompt for creating an account | **ca** | Enter your first name, last name and password |
| Display prompt for login in | **li** | Enter your account name and password |
| Display codes for navigation | **successful login** | Choose an option: cc - Create Credential, dc - Display Credentials, copy - Copy Credential or need a password generated for you. ex - exit |
| Display prompt for creating a credential | **cc** | Enter the account name, your username and password |
| Display a list of credentials | **dc** | list of saved credentials |
| Exit application | **ex** | Exit the current navigation stage |


## Testing the Application
* To run the tests for the class  and the credential file:

        $ python3.6 user_test.py
        $ python3.6 credentials_test.py

## Technologies Used
* Python3.6
