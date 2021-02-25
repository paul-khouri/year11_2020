import random

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
    global score
    A = X
    B = Y
    C = X - Y
    output = "{} - {} = ".format(A,B)
    answer = int(input(output))
    if answer == C:
        score += 1
        print("answer is correct")
    else:
        print("Sorry, the answer was {}".format(C))

def multiplying(X,Y):
    global score
    A = X
    B = Y
    C = X * Y
    output = "{} {} {} = ".format(A,chr(215),B)
    answer = int(input(output))
    if answer == C:
        score += 1
        print("answer is correct")
    else:
        print("Sorry, the answer was {}".format(C))

def dividing(X,Y):
    global score
    A = X
    B = Y
    C = X / Y
    output = "{} {} {} = ".format(A,chr(247),B)
    answer = int(input(output))
    if answer == C:
        score += 1
        print("answer is correct")
    else:
        print("Sorry, the answer was {}".format(C))

score = 0
total_questions = 0
# calling the functions
# we can do this as often as we like with lots of different values
adding(random.randint(5,25), random.randint(5,25))
total_questions += 1
subtracting(random.randint(5,25), random.randint(5,25))
total_questions += 1
multiplying(random.randint(5,25), random.randint(5,25))
total_questions += 1
# do something special
B=random.randint(5,25)
A = B*random.randint(5,25)
dividing(A, B)
total_questions += 1

print(score)
print(total_questions)

