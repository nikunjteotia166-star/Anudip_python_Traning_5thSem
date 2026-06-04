password = "admin123"

while True:
    user_password = input("Enter the password: ")

    if user_password == password:
        print("Login Successful!")
        break
    else:
        print("Incorrect password. Try again.")