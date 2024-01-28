# Importing functions from different modules
from adduser import add_user
from deluser import delete_user
from login import login
from passwd import change_password
from colorama import Fore, Style

# Function to print the menu
def print_menu():
    # Display the menu with colored options
    print(Fore.CYAN + Style.BRIGHT + "\n*************************************")
    print("*               Menu                *")
    print("*-----------------------------------*")
    print("* 1. " + Fore.GREEN + "Add User" + Fore.CYAN + "                       *")
    print("* 2. " + Fore.RED + "Delete User" + Fore.CYAN + "                    *")
    print("* 3. " + Fore.YELLOW + "Login" + Fore.CYAN + "                          *")
    print("* 4. " + Fore.MAGENTA + "Change Password" + Fore.CYAN + "                *")
    print("* 5. " + Fore.WHITE + "Quit" + Fore.CYAN + "                           *")
    print("*************************************" + Style.RESET_ALL)

# Main program logic
def main():
    # Continuously display the menu until the user chooses to quit
    while True:
        # Display the menu
        print_menu()

        # Get user input for menu choice
        choice = input(Fore.CYAN + "Select an option (1-5): " + Style.RESET_ALL).strip()

        # Execute the corresponding function based on user choice
        if choice == '1':
            add_user()  # Call the function to add a user
        elif choice == '2':
            delete_user()  # Call the function to delete a user
        elif choice == '3':
            login()  # Call the function to perform login
        elif choice == '4':
            change_password()  # Call the function to change password
        elif choice == '5':
            print(Fore.GREEN + "Exiting the program. Goodbye!" + Style.RESET_ALL)
            break  # Exit the loop and end the program
        else:
            print(Fore.RED + "Invalid option. Please select a valid option." + Style.RESET_ALL)

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Call the main function to start the program
    main()
