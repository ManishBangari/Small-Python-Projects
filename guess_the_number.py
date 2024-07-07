import random

print("Hello! What is your name??")

my_name = input()

print("Well, " + my_name + ", I am thinking of a number between 1 and 20.")


number = random.randint(1,20)
number_of_guesses = 6
number_found = False

while(number_of_guesses>=0 and not number_found):

    number_of_guesses-=1

    print("Take a guess.")
    guess = input()
    guess = int(guess)
    if guess == number:
        guesses = str(6 - number_of_guesses)
        print("Good job, " + my_name + "! You guessed the number in " + guesses + " guesses!")
        number_found=True

    else:
        if guess > number:
            print("Your guess is too high.")

        else:
            print("Your guess is too low.")


if not number_found:
    print("Unfortunately! " + my_name + " You didn't guessed the number. The number is "  + str(number))

