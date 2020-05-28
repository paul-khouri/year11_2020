import random
def addition_question():
    a = random.randint(5,9)
    b = random.randint(7,10)
    my_sum = a + b
    print("{} + {} =".format(a,b), end="")
    return my_sum


question_number = addition_question()
answer = int(input(" "))
if answer == question_number:
    print("Correct")
