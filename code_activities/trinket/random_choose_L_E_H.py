import random
lower = 4
higher = 15
my_random = random.randint(lower,higher)
middle_number = round((lower + higher)/2)
#print(middle_number)
#print(my_random)

print("A random number has been chosen between {} and {}".format(lower, higher))
print(40*"-")
guess = input("Enter L if you think the number is less than {0} \n"
              "Enter G if you think the number is more than {0} \n"
              "Enter E if you think the number is equal to {0} : ".format(middle_number))

if guess == "L" and my_random < middle_number:
  print("you win")
elif guess == "G" and my_random > middle_number:
  print("you win")
elif guess == "E" and my_random == middle_number:
  print("you win")
elif guess != "G" and guess != "L" and guess != "E":
  print("you have not entered an appropriate letter")
else:
  print("you lose")
print("The number was {}".format(my_random))
