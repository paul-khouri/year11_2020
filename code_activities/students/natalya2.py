import random

print("Welcome to the Higher Lower game")
print("You have 8 guesses to guess a randomly generated number between 0 & 10")

low = 0
high = 10

play_again = ""
while play_again == "":
    secret_number = random.randint(low,high)
    print(secret_number)
    # now has an inside loop that will run 8 times
    # it will break out if the user gets it right
    count = 8
    while count>0:
        have_integer=False
        while have_integer is False:
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
        # must lower the count value at the end of the inner loop
        count -= 1
    # if user enters 5 then play_again will still be 5
    # so the outer loop will run again
    play_again = input("Press <Enter> to play a round or Q to quit")

print("loop has ended")
