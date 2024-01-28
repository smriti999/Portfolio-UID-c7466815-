import getpass
import bcrypt

def delete_user():
    # Prompt the user for the username and password to delete the user
    username = input("Enter username to delete: ").strip()
    password = getpass.getpass("Enter your password to confirm deletion: ").strip()

    # Read existing user information from the password file
    with open('passwd.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Extract usernames and corresponding passwords from existing lines
    user_passwords = {line.split(':')[0]: line.split(':')[2] for line in lines}

    # Check if the provided username exists
    if username not in user_passwords:
        print("User not found. Nothing changed.")
        return

    # Check if the provided password is valid
    if not bcrypt.checkpw(password.encode(), user_passwords[username].encode()):
        print("Invalid password. User deletion aborted.")
        return

    # Create a new list excluding the lines with the specified username
    new_lines = [line for line in lines if line.split(':')[0] != username]

    # Write the modified content back to the password file
    with open('passwd.txt', 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

    print("User Deleted.")

if __name__ == "__main__":
    # Call the delete_user function when the script is run
    delete_user()
