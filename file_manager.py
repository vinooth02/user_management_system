import hashlib
import hmac
import os


class FileManager:

    def __init__(self, filename="users.txt"):
        self.filename = filename
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        if not os.path.exists(self.filename):
            with open(self.filename, "w", encoding="utf-8"):
                pass

    def _hash_password(self, password):
        return hashlib.sha256(
            password.encode("utf-8")
        ).hexdigest()

    def get_users(self):
        users = {}

        with open(self.filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                parts = line.split(",", 1)

                if len(parts) == 2:
                    username, password_hash = parts
                    users[username] = password_hash

        return users

    def user_exists(self, username):
        users = self.get_users()
        return username in users

    def save_user(self, username, password):
        if self.user_exists(username):
            return False

        password_hash = self._hash_password(password)

        with open(self.filename, "a", encoding="utf-8") as file:
            file.write(f"{username},{password_hash}\n")

        return True

    def verify_password(self, username, password):
        users = self.get_users()

        if username not in users:
            return False

        entered_hash = self._hash_password(password)
        stored_hash = users[username]

        return hmac.compare_digest(entered_hash, stored_hash)