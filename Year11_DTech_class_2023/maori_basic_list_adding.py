import random
A=[1,2,3,4,5]
B=["tahi", "rua", "toru", "whā", "rima", "ono", "whitu", "waru", "iwa", "tekau" ]

c = 0
while c<5:
    x=random.choice(A)
    y=random.choice(A)
    print(x)
    print(y)
    z=x+y
    question="{} + {} = ".format(B[x-1], B[y-1])
    answer=int(input(question))

    if answer == z:
        output = "Yeah, the answer was {}".format(B[z-1])
    else:
        output = "Oh no! The answer was {}".format(B[z-1])

    print(output)
    c+=1
    
