import random
import string

def generate_password(length):
    # All possible characters
    characters = string.ascii_letters + string.digits + string.punctuation
    # Randomly choose characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User input
length = int(input("Enter the desired password length: "))

# Generate password
password = generate_password(length)

# Display password
print("Generated Password:", password)
