import random

print("Hello welcome to the game!")

number_to_guess = random.randint(1,100)

while True:
    try:
        user_input =int(input("Guest a number between 1-100: "))
        if user_input < number_to_guess:
            print("too low!")
        elif user_input > number_to_guess:
            print("too high!")
        else:
            print("You won!")
            break

    except ValueError:
        print("Please enter a valid number! ")

