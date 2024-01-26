def change_password():
    """
    Change user password.
    """
    # Get user input for username and current password
    username = input("User: ").strip()
    current_password = input("Current Password: ").strip()

    # Read all lines from the 'passwd.txt' file
    with open('passwd.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Open the 'passwd.txt' file in write mode to update it
    with open('passwd.txt', 'w', encoding='utf-8') as file:
        user_found = False
        # Iterate through each line in the file
        for line in lines:
            existing_username, _, existing_password = line.split(':')
            # Check if the current line corresponds to the specified username
            if existing_username == username:
                user_found = True
                # Check if the provided current password is correct
                if existing_password.strip() == current_password:
                    # Get and confirm the new password
                    new_password = input("New Password: ").strip()
                    confirm_password = input("Confirm: ").strip()

                    # Update the password if the new and confirmed passwords match
                    if new_password == confirm_password:
                        file.write(f'{username}:{existing_username}:{new_password}\n')
                        print("Password changed.")
                    else:
                        print("Passwords do not match. No change made.")
                else:
                    print("Invalid current password. No change made.")
            else:
                # Write the line back to the file if the username does not match
                file.write(line)

        # Print a message if the specified user is not found
        if not user_found:
            print("User not found. Nothing changed.")

# Call the change_password function directly when the script is executed
change_password()
