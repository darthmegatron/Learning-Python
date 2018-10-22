# This is a sample random number guessing game.
from random import randrange
import manage_user


def login():
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


users = []
passw = {}
page = 0
while page == 0:
    print()  # Used for spacing in the console.
    print("********** Welcome to the Random Number Game! **********")
    print()  # Used for spacing in the console.
    new_or_existing = (input("New(1) or Returning User(2)?.."))
    print()  # Used for spacing in the console.

    if int(new_or_existing) == 1:
        users.append(manage_user.create_user())
        user = users[(len(users) - 1)]
        passw[user] = manage_user.create_password()

    elif int(new_or_existing) == 2:
        page += login()

    else:
        print("Please select an available option.")

print()  # Spacing

number = randrange(1, 10)


def guess():
    print("""Hey %s, pick a number from 1 to 10
    """ % (user.upper()))
    selection = 0
    attempts = 0

    while int(selection) != number:
        selection = input()

        if int(selection) == number:
            attempts += 1
            print("""
Good Job! You guessed the number in %d attempts!
            """ % attempts)

        elif int(selection) > 10 or int(selection) < 1:
            attempts += 1
            print("""
Please choose a number from 1 to 10
            """)

        elif int(selection) > number:
            attempts += 1
            print("""
It's lower than that. Try again.
            """)

        elif int(selection) < number:
            attempts += 1
            print("""
It's higher than that. Try again.
            """)


guess()

