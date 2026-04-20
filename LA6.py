# login_system.py

correct_username = "admin"
correct_password = "12345"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username:
    if password == correct_password:
        print("Welcome! Login successful.")
    else:
        print("Incorrect password.")
else:
    print("User not found.")
