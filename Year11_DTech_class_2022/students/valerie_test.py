import random

Q = ["France", "Germany", "Italy", "Russia", "Spain", "Portugal"]
A = ["Paris", "Berlin", "Rome", "Moscow", "Madrid", "Lisbon"]
Set = ["Q", "A", "B", "C", "D"]


def create_question(l):
    if len(l) != 6:
        print("The array for the question is the wrong size")
        return None
    
    question=[
        "What is the capital of {}?".format(l[0]),
        "A: {}".format(l[1]),
        "B: {}".format(l[2]),
        "C: {}".format(l[3]),
        "D: {}".format(l[4]),
        "{}".format(l[5])
    ]
    return question

c = 0
i = 0
while c <100:
    question_list = [""]*6
    #i = random.randint(0,len(Q)-1)
    i = i%len(Q)
    print(i)
    
    j = random.randint(1,4)
    question_list[0] = Q[i]
    question_list[j] = A[i]
    question_list[-1] = Set[j]

    while question_list.count("") > 0:
        wrong_answer = random.choice(A)
        if wrong_answer != A[i]:
            k = question_list.index("")
            question_list[k] = wrong_answer

    print(create_question(question_list))
    i += 1
    c += 1
