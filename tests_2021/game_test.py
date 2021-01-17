import random

Maori_list = ["Aotearoa","aroha","awa","haka","hangi","hapu",
              "hīkoi","hui","iti","iwi","kai","karakia",
              "kaumatua","kauri","kiwi","koha","kōhanga reo"]
English_list = ["New Zealand, long white cloud","love","river",
              "generic term for Māori dance.","traditional feast prepared in earth oven",
              "clan, sub-tribe; to be born ","walk","gathering, meeting","small","tribe",
              "food","prayer","elder","large native conifer","native flightless bird","gift, present "
              ,"language nest, Maori immersion pre-school "]

max_index = 0
# check all okay
if len(Maori_list) == len(English_list):
    print("all good, lists are the same length")
    max_index = len(Maori_list)-1



random_question_num = random.randint(0,len(Maori_list))


print(Maori_list[random_question_num])
print(English_list[random_question_num])


def correct():
    random_question_num = random.randint(0,max_index)
    output_string = "The word {} means {}".format(Maori_list[random_question_num], English_list[random_question_num])
    print(output_string)
    print("True or False?")

def incorrect():
    random_m_word_int = random.randint(0,max_index)
    random_e_word_int = random_m_word_int
    while random_e_word_int == random_m_word_int:
        random_e_word_int = random.randint(0,max_index)
    output_string = "The word \"{}\" means \"{}\" ".format(Maori_list[random_m_word_int], English_list[random_e_word_int])
    print(output_string)
    print("True or False?")
    
count = 0   
while count < 100:
    correct()
    incorrect()
    count+=1
    


