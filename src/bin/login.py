'''
Callopi User Login
Author: Christian Alvarez
Date: 10/29/2023
'''
from getpass4 import getpass
from utils import CUtils, FileConfig


class Login:
    def Shlogin():
        count: int = 0

        # Give users 5 tries to log in
        # Deny access if the user runs out of tries
        # Check if the user has valid credentials
        while count < 5:
            username: str = input('Username: ')
            password: str = getpass('Password: ')

            if CUtils.checkUserValid(username, password):
                print(f'Welcome Back, {username}!')
                return True
                break
            else:
                print('Username or Password is invalid. Try again.\n')
                count += 1
        else:
            print('Access denied')
            quit()

    def Guilogin(username, password):
        config = FileConfig()
        count = 0

        # check the data from the elements and compare the data from said element to the data in the credentials.yaml file
        # if the credentials are valid allow the user access into thhe program
        # if not deny them access
        while count < 5:
            if CUtils.checkUserValid(username, password):
                return 2
                break
            else:
                count += 1
        else:
            return -1
            
        

