import random
import string

print("=== Password Generator ===")

# Ask user for length
length = int(input("Enter password length: "))

# Characters to choose from
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = "".join(random.choice(characters) for _ in range(length))

print("\nYour Password is:", password)
