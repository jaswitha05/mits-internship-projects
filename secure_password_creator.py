import random
import string

def create_secure_password(pwd_length):
    available_chars = string.ascii_letters + string.digits + "!@#$%^&*()_+=-"
    password_chars = random.sample(available_chars, pwd_length)
    final_password = "".join(password_chars)
    return final_password

try:
    size = int(input("Enter the number of characters for your password: "))
    if size < 4:
        print("Password length should be at least 4 characters.")
    else:
        generated = create_secure_password(size)
        print("🔒 Your Secure Password:", generated)
except ValueError:
    print("Please enter a valid number.")
