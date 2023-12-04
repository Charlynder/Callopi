import unittest
from unittest.mock import patch
import io
from bin.login import Login  # Replace 'your_module_name' with the actual name of your module

class TestLogin(unittest.TestCase):

    def test_create_credentials(self):
        # Prepare input for the test
        input_data = "test_user\npassword123"
        with patch('builtins.input', side_effect=input_data.split('\n')):
            with patch('getpass4.getpass', return_value="password123"):
                # Redirect standard output to capture printed messages
                with io.StringIO() as output_buffer:
                    with patch('sys.stdout', new=output_buffer):
                        Login.createCredentials()

        # You can add more assertions to check if the file was created, etc.
        # For example, you can check if the file 'usr/credentials.yaml' exists.

    def test_check_user_valid(self):
        # Simulate a user with valid credentials
        username = "test_user"
        password = "password123"

        with patch('builtins.input', side_effect="\n".split('\n')):
            with patch('getpass4.getpass', side_effect="\n"):
                with patch('yaml.safe_load', return_value={'Username': 'test_user', 'Password': 'password123'}):
                    self.assertTrue(Login.check_user_valid(username, password))

        # Test with invalid credentials
        with patch('builtins.input', side_effect="\n".split('\n')):
            with patch('getpass4.getpass', side_effect="\n"):
                with patch('yaml.safe_load', return_value={'Username': 'test_user', 'Password': 'wrong_password'}):
                    self.assertFalse(Login.check_user_valid(username, password))

    def test_login(self):
        with patch('builtins.input', side_effect=["test_user", "wrong_password"] * 5):
            with patch('getpass4.getpass', return_value="wrong_password"):
                with patch('sys.exit') as exit_mock:
                    Login.login()
                    exit_mock.assert_called_with(0)  # Verify that sys.exit was called

if __name__ == '__main__':
    unittest.main()