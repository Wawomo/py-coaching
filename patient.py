#patient arrives
def get_username():
    while True:
        username = input("Enter a username (3-15 characters, letters and numbers only): ")
        
        if 3 <= len(username) <= 15 and username.isalnum():
            print("Username accepted:", username)
            break  # Exit the loop if the username is valid
        else:
            print("Error: Username must be 3-15 characters long and contain only letters and numbers.")

# Call the function
get_username()

def get_password():
    while True:
        password = input("Enter a password (6-8):")
        if 6 <= len(password) <= 8 and password.isalnum():
            print("password accepted:", password)
            break # Exit the loop if the password is valid
        else:
            print("Error: password must 6-8 characters")
# call the function
get_password()