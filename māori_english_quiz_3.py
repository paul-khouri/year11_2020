import random
from datetime import datetime
def create_results_file():
    confirm = input("Eeeeek! This will delete and create a fresh file, all data will be deleted. Y or N!")
    if confirm == "Y":
        write_file=open("results.csv", mode="w")
        header = "Date, Name, Score, Questions\n"
        write_file.write(header)
        write_file.close()
        print("Fresh file created")

def add_result(r):
    result= r
    write_file = open("results.csv", mode="a")
    write_file.write(result)
    write_file.close()

def print_results():
    write_file = open("results.csv", mode="r")
    for x in write_file:
        print(x, end="")


def read_file(level):
    E=[]
    M=[]
    my_file=open("Māori_Dictionary_levels.csv", mode="r")
    # skip first line
    my_file.readline()
    for line in my_file:
        #print(line, end="")
        line = line.replace("\n", "")
        line = line.strip()
        my_list = line.split(",")
        if(len(my_list) != 3):
            print(line)
            print("Problem")
            return None
        if int(my_list[2].strip()) == level:
            M.append(my_list[0].strip())
            E.append(my_list[1].strip())
        #print(my_list)
    return M, E


def create_date_string():
    my_date = datetime.now()
    my_string = my_date.strftime("%H:%M %d/%m/%Y")
    return my_string

      


def macron_check(a):
    word= a
    macron = ["ī","ā", "ō", "ū"]
    char = ["i","a", "o", "u"]
    for c in word:
        if c in ["ī","ā", "ō", "ū"]:
            word = word.replace(c, char[macron.index(c)])
    return word



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

def get_string(m, _min = 2):
    have_string = False
    my_string = ""
    while have_string is False:
        user_input = input(m)
        if len(user_input) < _min:
            print("The entry is too short in length")
            continue
        return user_input
        
    

#   --- running quiz
M, E =read_file(2)
#print(len(M))
#print(len(E))

c = list(zip(M, E))
random.shuffle(c)
M, E = zip(*c)  
            
player_name = get_string("Please enter your player name: ")      
question_number = get_integer("How many questions would you like? Choose between 5 and 10: ", 5,10)
print("-"*20)
score=0
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
        score += 1
        print("Brilliant")
    else:
        print("Unfortunately this is not correct")
        response = "the Māori word for '{}' is '{}'.".format(E[c], M[c])
        print(response)
    print("-"*20)
    c += 1

feedback = "Hi {} you scored {} points out of {}".format(player_name, score, question_number)
print(feedback)

result = "{},{},{},{}\n".format(create_date_string(), player_name, score, question_number)
print(result)
create_results_file()
add_result(result)
print_results()


        

	
	
	
	
	
	
