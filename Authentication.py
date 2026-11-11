# Dictionary to store user wuthentication

authentication = {}

# Function to enter a new user
def enter_user():
    username = input('Enter a username:\n')

    # Check if username exists
    if username in authentication:
        print('Usename exixts')
    else:
        password = input('Enter a password:\n')
        authentication[username] = password

# Function to log in existing user
def login_user():
    username = input('Enter your username:\n')
    password = input('Enter your password:\n')

    # Check if authentication exists
    if username in authentication and authentication[username] == password:
        print('Login sucessful')
    else:
        print('Invalid username of password')

# Main menu
# Main menu
def authentication_system():
    while True:
        print("\n*** Basic Authentication System ***")
        print("1. Register, 2. Login, 3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            enter_user()
        elif choice == '2':
            login_user()
        elif choice == '3':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

# Run the authentication system
authentication_system()