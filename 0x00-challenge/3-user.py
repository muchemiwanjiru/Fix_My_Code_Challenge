import unittest

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def is_valid_password(self, password):
        return self.password == password

class TestUser(unittest.TestCase):
    def test_is_valid_password(self):
        user = User("Test User", "password123")
        self.assertTrue(user.is_valid_password("password123"))
        self.assertFalse(user.is_valid_password("wrongpassword"))

if __name__ == "__main__":
    unittest.main()
