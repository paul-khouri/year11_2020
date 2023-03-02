import random

score = 0

def math_q(x,y,op):
    A= ["kore", "tahi", "rua", "toru" , "whā", "rima", "ono", "whitu", "waru", "iwa", "tekau"]
    # connect to the score variable outside the function
    
    global score

    # check which operator is being used and then do that operation for z
    if op == "+":
        z=x+y
    elif op == "-":
        z=x-y
    elif op == "*":
        z=x*y
    else:
        z=x/y

        
     # a bit of fancy stuff to give the right maths operator symbol   
    if op == "/":
        op = chr(247)
    elif op == "*":
        op = chr(215)

        
    # check if the value for x is 10 or less
    # if it is we can make the printed out number one of the words from the list
    if x <= 10:
        num_one = A[x]
    else:
        num_x = x
        
    if y <= 10:
        num_y = A[y]
    else:
        num_two = y
    # phew! we have everything now
    question = "{} {} {} = ".format(num_x,op,num_y)
    answer = int(input(question))
    if answer == z:
        score += 1
        print("Great")
    else:
        print("Nice try")

num_questions = 8
i = 0
while i < num_questions:
    # generate two random numbers for x and y
    x= random.randint(0,10)
    y=random.randint(0,10)
    if i%4 == 0:
        math_q(x,y,"*")
    elif i%4 == 1:
        # make sure division gives whole number
        a= x*y
        math_q(a,y,"/")
    elif i%4 == 2:
        math_q(x,y,"+")
    elif i%4 == 3:
        math_q(x,y,"-")
    i += 1
    
output = "Your score is {} out of {}".format(score, num_questions)
print(output)
    