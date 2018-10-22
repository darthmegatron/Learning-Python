# Stick with it this time Rob, your family is depending on it.

print()  # Used for spacing in the console.
print("Odd or Even?")
print()  # Used for spacing in the console.
number1 = input("Please enter a number... " )

print()  # Used for spacing in the console.
print("Your number is " + number1)
print()  # Used for spacing in the console.
value = (int(number1) % 2)
if value == 0:
    print(str(number1) + " is an even number!")

else:
    print(str(number1) + " is an odd number!")
