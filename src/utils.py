'''
Callopi Utils Service
Author: Christian Alvarez
Date: 10/30/2023
'''
import os
import json
from dataclasses import dataclass
from getpass4 import getpass

@dataclass
class FileConfig:
    credentialFile: str = 'src/config/credentials.json'

class CUtils:
    def fileExist(file):
        # check if the file exists
        fileExist = os.path.exists(file)

        if not fileExist:
            return False

    def createCredentials():
        # Get the file location from FileConfig
        config = FileConfig()

        # check if the file exists
        if not CUtils.fileExist(config.credentialFile):
            print(f'file "{config.credentialFile}" not found')

        print(' -------- Welcome to Callope! -------- \n')
        newUser: str = input('Create your Username: ')
        newUserPassword: str = getpass('Create a new Password: ')

        try:
            # Write data to the file
            user_data = {
                "Username": newUser,
                "Password": newUserPassword,
                "Admin": False
            }
            with open(config.credentialFile, 'w') as file:
                json.dump(user_data, file, indent=4)
            print(f'User credentials created. Stored at {config.credentialFile}')
        except FileNotFoundError:
            # Handle the case when the file is not found
            print('File not found!')

    def isAdmin(user):
        # get the file location from the FileConfig data
        config = FileConfig()

        # check if the file exists
        if not CUtils.fileExist(config.credentialFile):
            print(f'There is no file to see if the user is an admin')

        # check if the user labeled as an admin
        try:
            with open(config.credentialFile, 'r') as file:
                data = json.load(file)

            if data['Username'] == user and data['Admin'] is False:
                return True
        except Exception as e:
            print(f'An error occurred: {str(e)}')

    def checkUserValid(username, password):
        # Get the file location from FileConfig
        config = FileConfig()

        try:
            # Open the file
            with open(config.credentialFile, 'r') as file:
                data = json.load(file)

            # Check if the username and password entered by the user match the data in the JSON file
            if username == data['Username'] and password == data['Password']:
                return True
            else:
                return False
        except FileNotFoundError:
            # Handle the case when the file is not found
            return False
        except Exception as e:
            # Handle other exceptions
            print(f'An error occurred: {str(e)}')
            return False
