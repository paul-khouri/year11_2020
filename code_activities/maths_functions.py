def adding(X,Y):
    A = X
    B = Y
    C = X + Y
    output = "{} + {} = ".format(A,B)
    answer = int(input(output))
    if answer == C:
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


# calling the functions
# we can do this as often as we like with lots of different values
adding(70, 30)
subtracting(70, 30)
multiplying(80, 40)
dividing(80,40)
