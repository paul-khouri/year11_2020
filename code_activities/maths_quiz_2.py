import random
import dis
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
    return C

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

#f_list = [dividing,multiplying]
#print(f_list[0](2,3))
#g_list = [dividing(2,3), multiplying(2,3)]
#print(g_list[0])
print(type(adding))
#x=dis.dis(adding)
#print(x)
y=map(adding, (1,2,3), (1,2,3))
print(list(y))


    



