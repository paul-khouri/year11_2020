# this is importing the random module
import random
# start game loop
score = 0
total_played = 0
continue_program = True
while continue_program == True:
  # declaring the variables
  lower = 103
  higher = 307
  # finding the middle number
  mid_num= (lower+higher)/2
  mid_num = round(mid_num)
  # finding the random number
  random_num = random.randint(lower, higher)
  #instructions
  print("A random number has been chosen between {} and {}".format(lower, higher))
  print(40*"-")
  print("Choose L if you think the number is less than {0} \n"
                "Choose G if you think the number is more than {0} \n"
                "Choose E if you think the number is equal to {0} : ".format(mid_num))
  guess = input("Please enter your choice: -> ")
  # ensure input is upper case
  guess = guess.upper()
  # testing user response
  if guess == "L" and random_num < mid_num:
    score += 1
    print("you win")
  elif guess == "G" and random_num > mid_num:
    score += 1
    print("you win")
  elif guess == "E" and random_num == mid_num:
    score += 1
    print("you win")
  elif guess not in ["G", "L", "E"]:
    print("you have not entered an appropriate letter")
    total_played -= 1
  else:
    print("you lose")
  total_played += 1
  print("The number was {}".format(random_num))
  # find if user wants to play again
  user_input = input("Do you want to play again (Y/N)? ")
  #ensure input is upper case
  user_input = user_input.upper()
  if user_input != "Y":
      continue_program = False
      print("Thank you for playing")

print("You scored {} wins".format(score))
print("You played a total of {} games".format(total_played))
print("Program has ended")
    
      

