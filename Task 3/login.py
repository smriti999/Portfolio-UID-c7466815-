import hashlib

def generate_hash(password):
    """
    Generate hash for the given password using SHA-256.
    """
    sha256_hash = hashlib.sha256(password.encode()).hexdigest()
    return sha256_hash

def store_password(username, password):
    """
    Store the hashed password for the given username in 'passwd.txt'.
    Uncomment this line to create a new user.
    Adjust the paths and filenames as needed.
    """
    hashed_password = generate_hash(password)
    with open('passwd.txt', 'a', encoding='utf-8') as file:
        file.write(f"{username}:{hashed_password}\n")

def login():
    """
    Authenticate the user by checking the provided
    username and password against stored credentials.
    """
    username = input("User: ").strip()
    password = input("Password: ").strip()

    with open('passwd.txt', 'r', encoding='utf-8') as file:
        for line in file:
            existing_username, _, existing_password = line.strip().split(':')
            if (
                existing_username.lower() == username.lower()
                and generate_hash(password) == existing_password
            ):
                welcome_user(username)
                return

    print("Access denied.")

def welcome_user(username):
    """
    Display a welcome message for the authenticated user.
    """
    print(f"Welcome, {username}! Access granted.")

# Uncomment the following line to create a new user
# store_password("smriti", "ghalan")  # pylint: disable=unused-variable

# Call the login function directly when the script is executed
login()
