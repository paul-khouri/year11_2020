question_one = {
    "question" : "What does the Māori word  'maugna' mean?: ",
    "A" : "Sea",
    "B" : "Prestige",
    "C" : "Island",
    "D" : "Mountain",
    "answer" : "D"
    }

for x, y in question_one.items():
    if x == "question":
        print(y)
    else:
        output ="{} -- {}".format(x,y)
        print(output)
user_input = input("Please enter your choice: ")


    



    
