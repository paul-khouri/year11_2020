import random

Maori_list = ["Aotearoa","aroha","awa","haka","hangi","hapu",
              "hīkoi","hui","iti","iwi","kai","karakia",
              "kaumatua","kauri","kiwi","koha","kōhanga reo"
]
English_list = ["New Zealand, long white cloud","love","river",
              "generic term for Māori dance.","traditional feast prepared in earth oven",
              "clan, sub-tribe; to be born ","walk","gathering, meeting","small","tribe",
              "food","prayer","elder","large native conifer","native flightless bird","gift, present "
              ,"language nest, Maori immersion pre-school "]

Used_index_numbers=[]
score = 0

max_index = 0
max_count = 2
# check all okay
if len(Maori_list) == len(English_list):
    print("all good, lists are the same length")
    max_index = len(Maori_list)-1

def get_string_input(m):
    user_input = input(m)
    return user_input
def get_integer_input(m):
    user_input = int(input(m))
    return user_input


    


def run_question():
    Maori_word = ""
    English_correct = ""
    Question_list = []

    

    # randomly select maori word and its english meaning
    # select 3 other english words
    if len(Used_index_numbers) == len(Maori_list):
        print("all questions done")
        return None
    random_index = random.randint(0, max_index)
    while random_index in Used_index_numbers:
        random_index = random.randint(0, max_index)
    Used_index_numbers.append(random_index)
        

    Maori_word = Maori_list[random_index]
    English_correct = English_list[random_index]
    
    Question_list.append(English_correct)

    while len(Question_list)<4:
        random_index = random.randint(0, max_index)
        if English_list[random_index] not in Question_list:
            Question_list.append(English_list[random_index])


    message = "what is the meaning of {}".format(Maori_word.upper())
    print(message)
    print("-"*20)
    random.shuffle(Question_list)
    count = 0
    for x in Question_list:
        output_string = "{}: {}".format(count, Question_list[count])
        print(output_string)
        count += 1
    correct_index = Question_list.index(English_correct)
    print("-"*20)

    message = "Please choose correct option ->"
    response = get_integer_input(message)
    #response = correct_index
    if response == correct_index:
        print("Great")
        return 1
    else:
        print("Not quite right")
        return 0
cont = True
count = 0

while cont:
    result = run_question()
    if result is not None:
        score += result
        count += 1
    else:
        cont = False
    if count == max_count:
        cont = False
        

print(score)
print(len(Maori_list))








