import getpass
import bcrypt

def generate_hash(password):
    # Generate a random salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return salt, hashed_password.decode()

def store_password(username, real_name, password):
    # Store the username, salt, hashed password, and optional real name in a file
    salt, hashed_password = generate_hash(password)
    with open('passwd.txt', 'a', encoding='utf-8') as file:
        file.write(f"{username}:{salt}:{hashed_password}:{real_name}\n")

def add_user():
    # Prompt the user for new username, real name, and password
    username = input("Enter new username: ").strip()
    real_name = input("Enter real name: ").strip()

    while True:
        # Prompt for and validate the password
        password = getpass.getpass("Enter password: ").strip()
        if len(password) >= 8:
            break
        else:
            print("Invalid password. Please ensure it meets the criteria (at least 8 characters).")

    # Read existing usernames from the password file
    with open('passwd.txt', 'r', encoding='utf-8') as file:
        existing_usernames = {line.split(':')[0] for line in file}

        # Check if the provided username already exists
        if username in existing_usernames:
            print("Cannot add. Username already exists.")
            return

    # Store the new user information
    store_password(username, real_name, password)
    print("User Created.")

if __name__ == "__main__":
    # Call the add_user function when the script is run
    add_user()
