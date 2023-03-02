import random

def math_q(x,y,op):
    if op == "+":
        z=x+y
    elif op == "-":
        z=x-y
    elif op == "*":
        z=x*y
    else:
        z=x/y
    if op == "/":
        op = chr(247)
    elif op == "*":
        op = chr(215)
    question = "{} {} {} = ".format(x,op,y)
    answer = int(input(question))
    if answer == z:
        print("Great")
    else:
        print("Nice try")

        
math_q(6,2,"*")
math_q(6,2,"/")
math_q(6,2,"+")
math_q(6,2,"-")
    
