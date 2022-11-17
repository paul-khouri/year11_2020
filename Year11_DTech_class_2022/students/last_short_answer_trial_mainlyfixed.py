# put the words in one list for each language
M = ["Kei te pehea koe", "Nau mai haere mai"]
E = ["How are you" , "Welcome"]


c = 0
while c<2:

    answer = input("What is the Maori phrase for {}?". format(E[0]))
    if answer == M[0]:
        print("Good job")
    else:
        print("Incorrect")
        
    answer = input("What is the Maori word for {}?". format(E[1]))
    if answer == M[1]:
        print("Good job")
    else:
        print("Incorrect")
    # the c needed to be indented
    c +=1
