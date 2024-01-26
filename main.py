def main():
    # Main program for user management

    while True:
        # Display menu options to the user
        print("\nMenu:")
        print("1. Add User")
        print("2. Delete User")
        print("3. Login")
        print("4. Change Password")
        print("5. Quit")

        # Get user choice
        choice = input("Select an option (1-5): ").strip()

        if choice == '1':
            # Add User
            from adduser import add_user
            add_user()
        elif choice == '2':
            # Delete User
            from deluser import delete_user
            delete_user()
        elif choice == '3':
            # User Login
            from login import login
            login()
        elif choice == '4':
            # Change Password
            from passwd import change_password
            change_password()
        elif choice == '5':
            # Quit the program
            print("Exiting the program. Goodbye!")
            break
        else:
            # Invalid option
            print("Invalid option. Please select a valid option.")

# Call the main function directly to start the program
main()
