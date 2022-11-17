import random

def get_integer(m, _min, _max):
    have_integer = False
    user_input = 0
    while have_integer is False:
        try:
            user_input= int(input(m))
        except ValueError:
            print("Please enter a whole number")
            continue

        if user_input<_min or user_input >_max:
            message = "Please enter a value between {} and {}".format(_min, _max)
            print(message)
            continue

        return user_input

    
def macron_check(a):
    word= a
    macron = ["ī","ā", "ō", "ū"]
    char = ["i","a", "o", "u"]
    for c in word:
        if c in ["ī","ā", "ō", "ū"]:
            word = word.replace(c, char[macron.index(c)])
    return word

def read_file(level):
    print("Level passed as a parameter is: {}".format(level))
    E=[]
    M=[]
    my_file = open("Māori_Dictionary_levels.csv", mode="r")
    my_file.readline()
    for line in my_file:
        line = line.replace("\n", "")
        line = line.strip()
        my_list=line.split(",")
        
        if int(my_list[2]) == level:
            M.append(my_list[0].strip())
            E.append(my_list[1].strip())
    return E, M

    




#print(macron_check("hīkoi"))
level = get_integer("Which level would you like Easy(1) Medium(2) Hard(3) ? :", 1,3)

E,M = read_file(level)
# testing - make sure lists are the same length
print(len(M))
print(len(E))

# shuffle parallel lists
c = list(zip(M, E))
random.shuffle(c)
M, E = zip(*c)

question_number = get_integer("How many questions would you like? Choose between 5 and 10", 5,10)
            
        

c = 0
while c < question_number:
    question = "What is the Māori word for '{}' ?".format(E[c])
    answer = input(question).lower().strip()
    correct_answer = macron_check( M[c].lower().strip() )
    if answer == correct_answer:
        print("Brilliant")
    else:
        print("unfortunately this is not correct")
        response = "the Māori word for '{}' is '{}'.".format(E[c], M[c])
        print(response)
    c += 1
print("Program has ended")
