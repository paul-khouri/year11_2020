import random 
def read_file(level):
    E=[]
    M=[]
    my_file=open("Māori_Dictionary_levels.csv", mode="r")
    # skip first line
    my_file.readline()
    for line in my_file:
    
        line = line.replace("\n", "")
        line = line.strip()
        my_list = line.split(",")
        
        # error check
        if(len(my_list) != 3):
            print(line)
            print("Problem")
            return None
        
        if int(my_list[2].strip()) == level:
            M.append(my_list[0].strip())
            E.append(my_list[1].strip())
    return M, E
      
M, E =read_file(2)
print(len(M))
print(len(E))

c = list(zip(M, E))
random.shuffle(c)
M, E = zip(*c)

def macron_check(a):
    word= a
    macron = ["ī","ā", "ō", "ū"]
    char = ["i","a", "o", "u"]
    for c in word:
        if c in ["ī","ā", "ō", "ū"]:
            word = word.replace(c, char[macron.index(c)])
    return word

print(macron_check("hīkoi"))

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
    
    
            
        
question_number = get_integer("How many questions would you like? Choose between 5 and 10", 5,10)
print("-"*20)

c = 0
while c < question_number:
    m_word =  M[c].lower().strip()
    correct_answer = macron_check( m_word )
    message = [
        "-"*20,
        "For this question please enter answer without macrons",
        "(this will be automatically added)",
        "-"*20]
    if m_word != correct_answer:
        for x in message:
            print(x)
    question = "What is the Māori word for '{}' ?".format(E[c])
    answer = input(question).lower().strip()

    if answer == correct_answer:
        print("Brilliant")
    else:
        print("unfortunately this is not correct")
        response = "the Māori word for '{}' is '{}'.".format(E[c], M[c])
        print(response)
    print("-"*20)
    c += 1
print("Program has ended")
        

	
	
	
	
	
	
