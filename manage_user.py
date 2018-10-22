def create_user():
    username = (input("Username: "))
    if len(username) > 3:
        return username

    else:
        print('Username must be at least 3 characters.')
        create_user()


def create_password():
    password = (input("Password: "))
    if len(password) > 5:
        return password

    else:
        print("Password must be at least 5 characters.")
        create_password()
