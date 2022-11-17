import random
# set min max boundaries
min_num = 1
max_num = 10
# generate number
secret_num = random.randint(min_num, max_num)

output = "A secret number between {} and {} has been chosen.".format(min_num, max_num)
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
