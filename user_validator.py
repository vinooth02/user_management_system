class UserValidator:

    def validate_username(self, username):

        if len(username) != 8:
            return False

        if not username.isalnum():
            return False

        return True

    def validate_password(self, password):

        if len(password) < 8:
            return False

        has_uppercase = any(char.isupper() for char in password)
        has_lowercase = any(char.islower() for char in password)
        has_number = any(char.isdigit() for char in password)

        return has_uppercase and has_lowercase and has_number