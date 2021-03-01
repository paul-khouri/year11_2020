import random
score = 0

def adding(X,Y):
    global score
    A = X
    B = Y
    C = X + Y
    output = "{} + {} = ".format(A,B)
    answer = int(input(output))
    if answer == C:
        score += 1
        print("answer is correct")
    else:
        print("Sorry, the answer was {}".format(C))

def subtracting(X,Y):
    A = X
    B = Y
    C = X - Y
    output = "{} - {} = ".format(A,B)
    answer = int(input(output))
    if answer == C:
        print("answer is correct")
    else:
        print("Sorry, the answer was {}".format(C))

def multiplying(X,Y):
    A = X
    B = Y
    C = X * Y
    output = "{} {} {} = ".format(A,chr(215),B)
    answer = int(input(output))
    if answer == C:
        print("answer is correct")
    else:
        print("Sorry, the answer was {}".format(C))

def dividing(X,Y):
    A = X
    B = Y
    C = X / Y
    output = "{} {} {} = ".format(A,chr(247),B)
    answer = int(input(output))
    if answer == C:
        print("answer is correct")
    else:
        print("Sorry, the answer was {}".format(C))

counter = 0
while counter < 5:
    # calling the functions
    # we can do this as often as we like with lots of different values
    A = random.randint(30,80)
    B = random.randint(30,80)
    adding(A, B)
    # increment
    counter += 1


    



