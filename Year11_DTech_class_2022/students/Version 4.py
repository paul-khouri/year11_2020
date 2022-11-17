# Version Four

import random

#Declare lists
maori = ["Tāmaki Makaurau", "Te Whanganui-a-Tara", "Ōtautahi", "Ōtepoti", "Ōtākou",
         "Kirikiriroa", "Tāhuna", "Whakatū", "Ahuriri", "Rotorua", "Taupo",
         "Tauranga", "Waikato", "Te Moana a Toi", "Te Matau-a-Māui"]
english = ["Auckland", "Wellington", "Christchurch", "Dunedin", "Otago",
           "Hamilton", "Queenstown", "Nelson", "Napier", "Rotorua",
           "Taupo", "Tauranga", "Waikato", "Bay of Plenty", "Hawke's Bay"]
question_data = []
option_index = []
asked_questions = []
incorrect_questions = []
incorrect_answers = []

#Welcome User

print("-"*80)
print("Welcome to New Zealand in Words!")
print("-"*80)

#Collect user name and validate name input
name_valid = False
while name_valid == False:
    try:
        name = str(input("What is your name? "))
    except ValueError:
        print("You have not entered a valid name. Please try again. ")
        continue
    else:
        name_valid = True

#Print Instructions
print("-"*80)
print("Hello {}!".format(name))
print("""In this game:
1. You will be given the Maori name of a significant New Zealand location
2. You will need to answer the question by entering the corresponding number

eg. A. Auckland --> enter: A """)

#Start loop running game
running = True
while running == True:
    # Ask 15 questions
    question_count = 15
    #Set score to 0 at beginning
    score = 0

    while question_count > 0:
        #Ensure question will not be asked multiple times unless user gets it wrong.
        question_new = False
        while question_new == False:
            x = random.randint(0,len(english)-1)
            chosen_place = maori[x]
            if chosen_place not in asked_questions:
                asked_questions.append(chosen_place)
                question_new = True
            else:
                continue
        #Assigning values to question properties (eg. answer, index, options)
        correct_answer = english[x]

        #Store one question's worth of data
        option_index.append(x)

        #Ensure correct answer is in the options
        question_data.append(correct_answer)

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

        #Randomize options (so that correct option isn't always in the same position)
        random.shuffle(question_data)
        corresponding_letter = ["A", "B", "C", "D"]

        #Collect the correct answer (the corresponding letter)
        n = question_data.index(correct_answer)
        answer_letter = corresponding_letter[n]

        #Question
        question = ["What is {} in English?".format(chosen_place),
                      "A: {}".format(question_data[0]),
                      "B: {}".format(question_data[1]),
                      "C: {}".format(question_data[2]),
                      "D: {}".format(question_data[3]),
                      "{}".format(answer_letter)]

        #set starting index at 0
        x = 0

        #Receive input
        print("-" * 80)
        for i in range(0,5):
            print(question[i])

        #Recieve and validate user input
        valid = False
        while valid == False:
            user_answer = input("Please enter your response: ").upper().strip()
            if user_answer not in ["A", "B", "C", "D"]:
                print("You have entered an invalid input. Please try again.")
                continue
            else:
                valid = True

        #Process input and give relevant feedback
        if user_answer == answer_letter:
            print("That is correct.")
            score += 1
        else:
            print("That is incorrect.")
            #If incorrect, store incorrect question and the correct answer in incorrect_questions/answers
            #Also, remove it from asked_questions so it can be asked again.
            #If user has already got it wrong before, it can be asked again,
            #But does not need to be put in incorrect_questions/answers again (or will repeat at the end)
            if chosen_place not in incorrect_questions:
                incorrect_questions.append(chosen_place)
                incorrect_answers.append(correct_answer)
                asked_questions.pop()
            else:
                asked_questions.pop()

        #Recognize question has been asked and answered
        question_count -= 1

        #Clear spaces for new question
        question_data.clear()
        option_index.clear()

        

    print("-"*36 + "GAME ENDS" + "-"*35)

    #Give user their score
    print("Score: {}/15".format(score))

    #Show user questions they got wrong and what the correct answers were
    #Or congratulate for perfect score
    if score != 15:
        print("These are the questions you did not answer correctly:")
        for wrong_question, wrong_answer in zip(incorrect_questions,incorrect_answers):
        print("- {:<20} {}".format(wrong_question,wrong_answer))
    else:
        print("Congratulations on your perfect score!")
    
    print("-"*80)

    #Ask user if they would like to play again
    play_again = input("Would you like to play again (y/n)? ").lower().strip()

    #Respond accordinly to whether user wants to play again.
    if play_again == "y":
        asked_questions.clear()
        continue
    else:
        running = False
