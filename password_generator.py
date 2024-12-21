import random
import string

def password_generator():
    print("Welcome to the Random Password Generator!")
    
    # Ask the user for the length of the password
    try:
        length = int(input("Enter the desired password length (minimum 6): "))
        if length < 6:
            print("Password length should be at least 6 characters.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    print(f"Your random password is: {password}")

# Run the Password Generator
password_generator()
