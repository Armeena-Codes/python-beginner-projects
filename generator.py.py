# Random Password Generator - Python Beginner Project 3
# Created by Armeena-Codes
import random
import string

def generate_password(length=8):
    chars = string.ascii_letters + string.digits + "!@#$%"
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

print("=== Password Generator by Armeena ===")
length = int(input("Enter password length (e.g. 8): "))
print(f"Your new password: {generate_password(length)}")