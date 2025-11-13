# Ask for the user's name
name = input("Enter your name: ")

# Check if the name is Ryan
if name == "Ryan":
    print("Access granted.")
else:
    # Ask for a password if not Ryan
    password = input("Enter password: ")

    # Check the password
    if password == "12345":
        print("Access granted.")
    else:
        print("Error.")