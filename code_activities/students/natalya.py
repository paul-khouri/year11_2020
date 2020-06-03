import random

print("Welcome to the Higher Lower game")
print("You have 8 guesses to guess a randomly generated number between 0 & 10")

low = 0
high = 10

secret_number = random.randint(low,high)
print(secret_number)

play_again = int(input("Enter '5' to play a round"))
while play_again == 5:

    have_integer=False
    while have_integer == False:
        try:
            guess = int(input("What do you think the number is?"))
        except ValueError:
            print("integer has not been entered")
            continue
        have_integer = True

    if guess > secret_number:
        print("Your guess is greater then the number")
    elif guess < secret_number:
        print("Your guess is lower then the number")
    else:
        print("You are correct")
        print("Well done! You have guessed the number")
        break

print("loop has ended")
