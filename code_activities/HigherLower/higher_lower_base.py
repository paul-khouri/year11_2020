import random
min_num = 1 # set min max boundaries
max_num = 10
secret_num = random.randint(min_num, max_num) # generate number
output = "A secret number bewteen {} and {} has been chosen.".format(min_num, max_num)
print(output)
guess = int( input("Please enter your guess: ") )
# check user guess
if guess < secret_num:
    print("Your guess is too small")
elif guess > secret_num:
    print("Your guess is too large")
elif guess == secret_num:
    print("You guessed it!")
else:
    print("Error")
# testing
output = "The number was {}".format(secret_num)
print(output)
