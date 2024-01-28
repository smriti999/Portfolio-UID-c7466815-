import bcrypt
import getpass

def generate_hash(password):
    # Generate a random salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return salt, hashed_password.decode()

def store_password(username, real_name, password):
    # Store the username, salt, hashed password, and optional real name in a file
    salt, hashed_password = generate_hash(password)
    with open('passwd.txt', 'a', encoding='utf-8') as file:
        file.write(f"{username}:{salt.decode()}:{hashed_password}:{real_name}\n")

def change_password():
    # Prompt the user for username and current password
    username = input("Enter username: ").strip()
    current_password = getpass.getpass("Current Password: ").strip()

    # Read existing user information from the password file
    with open('passwd.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    user_found = False
    modified_content = []

    # Iterate through each line in the file to find the user
    for line in lines:
        parts = line.strip().split(':')
        if len(parts) >= 3:
            existing_username, existing_salt, existing_hashed_password = parts[:3]

            # Check if the current line corresponds to the provided username
            if existing_username == username:
                user_found = True

                # Check if the provided current password is valid
                if bcrypt.checkpw(current_password.encode(), existing_hashed_password.encode()):
                    # Prompt for and update the password if the current password is valid
                    new_password = getpass.getpass("New Password: ").strip()
                    confirm_password = getpass.getpass("Confirm Password: ").strip()

                    # Confirm the new password and update the file accordingly
                    if new_password == confirm_password:
                        real_name = parts[3] if len(parts) > 3 else ""  # Get the real name if available
                        salt, hashed_password = generate_hash(new_password)
                        modified_content.append(f"{username}:{salt.decode()}:{hashed_password}:{real_name}\n")
                        print("Password changed.")
                        continue
                    else:
                        print("Passwords do not match. No change made.")
                else:
                    print("Invalid current password. No change made.")
            else:
                modified_content.append(line)

    # If the user is not found, indicate that no changes were made
    if not user_found:
        print("User not found. Nothing changed.")

    # Write the modified content back to the password file
    with open('passwd.txt', 'w', encoding='utf-8') as file:
        file.writelines(modified_content)

if __name__ == "__main__":
    # Call the function to change the password when the script is run
    change_password()
