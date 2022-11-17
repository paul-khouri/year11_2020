import random

def check_answer(C,m):
    answer = int(input(m))
    if answer == C:
        print("answer is correct")
        return 1
    else:
        print("Sorry, the answer was {}".format(C))
        return 0
    

def adding(X,Y):
    C = X + Y
    output = "{} + {} = ".format(X,Y)
    return check_answer(C, output)
 

def subtracting(X,Y):
    C = X - Y
    output = "{} - {} = ".format(X,Y)
    return check_answer(C, output)
  

def multiplying(X,Y):
    C = X * Y
    output = "{} {} {} = ".format(X,chr(215),Y)
    return check_answer(C, output)

def dividing(X,Y):
    C = X / Y
    output = "{} {} {} = ".format(X,chr(247),Y)
    return check_answer(C, output)
        
# set variables score and total_questions
questions = [adding, subtracting, multiplying, dividing]
score = 0
total_questions = 0
# setting counter for loop
counter = 0
#starting loop
while counter < 5:
    A = random.randint(2, 30)
    B = random.randint(2, 30)
    # randomly determine which type of question to run
    question_index = random.randint(0,3)
    if question_index == 3:
        A = random.randint(2,7)*B
        questions[question_index](A,B)
    else:
        questions[question_index](A,B)

    total_questions += 1
    counter += 1
#end of loop, print feedback
    
output = "You scored {} out of {}".format(score, total_questions)
print(output)

