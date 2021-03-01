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
    # randomly determine which type of question to run
    question_type = random.randint(1,4)
    A = random.randint(2, 30)
    B = random.randint(2, 30)
    if question_type == 1:
        adding(A,B)
    elif question_type == 2:
        subtracting(A,B)
    elif question_type == 3:
        multiplying(A,B)
    elif question_type == 4:
        # make sure division is a whole number result
        A = random.randint(2,7)*B
        dividing(A,B)
    total_questions += 1
    counter += 1
#end of loop, print feedback
    
output = "You scored {} out of {}".format(score, total_questions)
print(output)

