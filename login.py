# Dictionary key pair practice.
import manage_user


def login():
    print(users)  # Testing
    print(passw)  # Testing
    username = (input("Enter Username: "))
    password = (input("Enter password: "))
    if username in users and password == passw[username]:
        print()  # Used for spacing in the console.
        print("Authenticated")
        return 1
    else:
        print()  # Used for spacing in the console.
        print("Username or Password is incorrect.")
        return 0


page = 0
while page == 0:
    users = []
    passw = {}
    print()  # Used for spacing in the console.
    print("********** Welcome to the login test page! **********")
    print()  # Used for spacing in the console.
    new_or_existing = (input("New(1) or Returning User(2)?.."))
    print()  # Used for spacing in the console.

    if int(new_or_existing) == 1:
        users.append(manage_user.create_user())
        user = users[(len(users) - 1)]
        print(user)  # Testing
        passw[user] = manage_user.create_password()
        print(users)  # Testing
        print(passw)  # Testing

    elif int(new_or_existing) == 2:
        page = login()

    else:
        print("Please select an available option.")
