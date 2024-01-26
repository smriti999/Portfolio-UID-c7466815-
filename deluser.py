def delete_user():
    """
    Delete a user by providing the username.
    """
    # Get the username to be deleted from user input
    username = input("Enter username: ").strip()

    # Read all lines from the 'passwd.txt' file
    with open('passwd.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Initialize a flag to check if the user was found
    user_found = False

    # Open the 'passwd.txt' file in write mode to update it
    with open('passwd.txt', 'w', encoding='utf-8') as file:
        # Iterate through each line in the file
        for line in lines:
            # Extract the existing username from the line
            existing_username = line.split(':')[0]

            # Check if the current line does not correspond to the username to be deleted
            if existing_username != username:
                # Write the line back to the file if the username does not match
                file.write(line)
            else:
                # Set the user_found flag to True if the username is found
                user_found = True

    # Print a message based on whether the user was found or not
    if user_found:
        print("User Deleted.")
    else:
        print("User not found. Nothing changed.")

# Call the delete_user function directly when the script is executed
delete_user()
