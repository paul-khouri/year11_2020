# this is importing the random module
import random

# declaring the variables
lower = 103
higher = 307
# finding the middle number
mid_num= (lower+higher)/2
mid_num = round(mid_num)
random_num = random.randint(lower, higher)
print("A random number has been chosen between {} and {}".format(lower, higher))
print(40*"-")
print("Choose L if you think the number is less than {0} \n"
              "Choose G if you think the number is more than {0} \n"
              "Choose E if you think the number is equal to {0} : ".format(mid_num))
guess = input("Please enter your choice: -> ")

if guess == "L" and random_num < mid_num:
  print("you win")
elif guess == "G" and random_num > mid_num:
  print("you win")
elif guess == "E" and random_num == mid_num:
  print("you win")
elif guess not in ["G", "L", "E"]:
  print("you have not entered an appropriate letter")
else:
  print("you lose")
print("The number was {}".format(random_num))

