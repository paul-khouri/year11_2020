import math
import random
# number list to generate all numbers up to 99
number_list=["kore", "tahi", "rua" , "toru", "whā", "rima", "ono",
                         "whitu","waru","iwa", "tekau"]
# user score 
score = 0

#function to translat an integer into the Māori word for the number (up to 99)
def numbers_to_hundred(n):
    # declare empty output string
    output = ""
    # create string based on value of number
    if n <= 10:
        output = number_list[n]
    elif n%10 == 0:
        lead_digit = math.floor(n/10)
        output = "{} {}".format(number_list[lead_digit], number_list[10])
    elif n < 20:
        output = "tekau mā {}".format(number_list[n%10])
    elif n<100:
        output = "{} tekau mā {}".format( number_list[math.floor(n/10)], number_list[n%10])
    return output

# test function to see if numbers correctly generated      
def to_one_hundred():
    c= 0
    while c < 100:
        numbers_to_hundred(c)
        c += 1
    
    
# takes two integers as arguments
def adding(X,Y):
    global score
    A = X
    B = Y
    C = X + Y
    # get numbers as words in Māori
    A_M=numbers_to_hundred(A)
    B_M=numbers_to_hundred(B)
    # print question
    help_sum = "{} + {} = ".format(A,B)
    print(help_sum)
    outsum= "{} + {} = ".format(A_M,B_M)
    # request user input
    answer = int(input(outsum))
    # cehck answer and give feedback
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
    A_M=numbers_to_hundred(A)
    B_M=numbers_to_hundred(B)
    help_sum = "{} - {} = ".format(A,B)
    print(help_sum)
    output = "{} - {} = ".format(A_M,B_M)
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
    A_M=numbers_to_hundred(A)
    B_M=numbers_to_hundred(B)
    help_sum = "{} {} {} = ".format(A,chr(215),B)
    print(help_sum)
    output = "{} {} {} = ".format(A_M,chr(215),B_M)
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
    A_M=numbers_to_hundred(A)
    B_M=numbers_to_hundred(B)
    help_sum = "{} {} {} = ".format(A,chr(247),B)
    print(help_sum)
    output = "{} {} {} = ".format(A_M,chr(247),B_M)
    answer = int(input(output))
    if answer == C:
        score += 1
        print("answer is correct")
    else:
        print("Sorry, the answer was {}".format(C))
q=0
while q< 20:
    random_num = random.randint(1,4)
    X = random.randint(1,20)
    Y = random.randint(1,20)
    if random_num == 1:
        adding(X,Y)
    elif random_num == 2:
        subtracting(X,Y)
    elif random_num == 3:
        X = random.randint(1,10)
        Y = random.randint(1,10)
        multiplying(X,Y)
    elif random_num == 4:
        Z=random.randint(1,5)
        dividing(Z*X,X)
    else:
        print("random generator error")  
    q+=1



