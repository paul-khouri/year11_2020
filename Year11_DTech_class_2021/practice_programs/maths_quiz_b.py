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
        
# set variables score and total_questions
score = 0
total_questions = 0
# setting counter for loop
counter = 0
#starting loop
while counter < 5:
    A = random.randint(2, 19)
    B = random.randint(2, 19)
    adding(A,B)
    total_questions += 1
    counter += 1
#end of loop, print feedback
    
output = "You scored {} out of {}".format(score, total_questions)
print(output)

