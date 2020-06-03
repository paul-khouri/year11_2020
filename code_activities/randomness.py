# import the random number library
import random

#random number between 0 and 1
print(random.random())

# random number between two integers (inclusive)
print(random.randint(2,5))

# random number between two integers (inclusive)
# but with a step value (in this case will only get multiples
#of 5
print (random.randrange(0, 101, 5))

# create a list and randomly select a name from it
myList = ["Anna", "Michael", "Sarah", "Jessie"]
print(random.choice(myList))
