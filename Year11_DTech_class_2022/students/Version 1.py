# Version One

import random

#Declare lists
maori = ["Tāmaki Makaurau", "Te Whanganui-a-Tara", "Ōtautahi", "Ōtepoti", "Ōtākou"]
english = ["auckland", "wellington", "christchurch", "dunedin","otago"]
question_data = []
option_index = []

#Assigning values to question properties (eg. answer, index, options)
x = random.randint(0,len(english)-1)
x=4
chosen_place = maori[x]
correct_answer = english[x]

#Store one question's worth of data
option_index.append(x)
print(option_index)

#Ensure correct answer is in the options
question_data.append(correct_answer)
print(question_data)

#Generate three other different options
option_count = 3
while option_count > 0:
    y = random.randint(0,len(english)-1)
    if y not in option_index:
        question_data.append(english[y])
        option_index.append(y)
        option_count -= 1
    else:
        continue
print(question_data)


#Randomize options (so that correct option isn't always in the same position)
random.shuffle(question_data)
corresponding_letter = ["A", "B", "C", "D"]
print(question_data)

#Collect the correct answer (the corresponding letter)
n = question_data.index(correct_answer)
answer_letter = corresponding_letter[n]

#Question
question = ["What is {} in English?".format(chosen_place),
              "A: {}".format(question_data[0].capitalize()),
              "B: {}".format(question_data[1].capitalize()),
              "C: {}".format(question_data[2].capitalize()),
              "D: {}".format(question_data[3].capitalize()),
              "{}".format(answer_letter)]


#set starting index at 0
x = 0

#Receive input
print("-" * 50)
for i in range(0,5):
    print(question[i])
user_answer = input("Please enter your response: ").upper()

#Process input and give relevant feedback
if user_answer == answer_letter:
    print("That is correct.")
else:
    print("That is incorrect.")
