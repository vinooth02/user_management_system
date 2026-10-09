from user_validator import UserValidator
from file_manager import FileManager


class UserManager:

    def __init__(self):
        self.validator = UserValidator()
        self.file_manager = FileManager()

    def register_user(self, username, password):

        if not self.validator.validate_username(username):
            return False, "Username must be exactly 8 alphanumeric characters."

        if not self.validator.validate_password(password):
            return False, (
                "Password must contain at least 8 characters, "
                "one uppercase letter, one lowercase letter, "
                "and one number."
            )

        if self.file_manager.user_exists(username):
            return False, "User already exists."

        if self.file_manager.save_user(username, password):
            return True, "Registration successful."

        return False, "Registration failed."

    def login_user(self, username, password):

        if not self.file_manager.user_exists(username):
            return False, "User not found. Please create a new user."

        if self.file_manager.verify_password(username, password):
            return True, f"Welcome, {username}!"

        return False, "Incorrect password."