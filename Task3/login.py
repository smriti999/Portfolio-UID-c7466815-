import getpass
import bcrypt

def login():
    # Prompt the user for username and password
    username = input("User: ").strip()
    password = getpass.getpass("Password: ").strip()

    # Read existing user information from the password file
    with open('passwd.txt', 'r', encoding='utf-8') as file:
        for line in file:
            # Split the line into parts using ':' as the delimiter
            parts = line.strip().split(':')

            # Check if there are at least three parts
            if len(parts) >= 3:
                existing_username, existing_salt, existing_password = parts[:3]

                # Check if the current line corresponds to the provided username
                if existing_username.lower() == username.lower() and bcrypt.checkpw(password.encode(), existing_password.encode()):
                    # Authentication successful
                    real_name = parts[3] if len(parts) > 3 else "User"  # Get the real name if available
                    print(f"Welcome, {real_name}! Access granted.")
                    return

    # Authentication failed
    print("Access denied.")

if __name__ == "__main__":
    # Call the login function when the script is run
    login()
