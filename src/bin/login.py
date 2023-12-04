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


