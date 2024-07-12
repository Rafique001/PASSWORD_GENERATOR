import random
import string


class PasswordGenerator:
    def __init__(self, length=8):
        self.length = length

    def generate(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(self.length))
        return password

    def evaluate_strength(self, password):
        if len(password) < 6:
            return "Weak"
        elif len(password) < 10:
            return "Medium"
        else:
            return "Strong"
