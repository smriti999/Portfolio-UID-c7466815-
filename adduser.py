import getpass

def is_valid_password(password):
    # Simplified password validation (you can customize as needed)
    return len(password) >= 8

def add_user():
    """
    Add a new user to the system.
    """
    username = input("Enter new username: ").strip()
    real_name = input("Enter real name: ").strip()

    while True:
        password = getpass.getpass("Enter password: ").strip()
        if is_valid_password(password):
            break
        else:
            print("Invalid password. Please ensure it meets the criteria.")

    with open('passwd.txt', 'r', encoding='utf-8') as file:
        existing_usernames = [line.split(':')[0] for line in file]
        if username in existing_usernames:
            print("Cannot add. Most likely username already exists.")
            return

    with open('passwd.txt', 'a', encoding='utf-8') as file:
        file.write(f"{username}:{real_name}:{password}\n")

    print("User Created.")

# Call the add_user function directly when the script is executed
add_user()
