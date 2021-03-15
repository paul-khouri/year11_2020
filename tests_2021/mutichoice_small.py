question_one = ["What is the capital of Syria?",
                "A: Jordan",
                "B: Damascus",
                "C: Baghdad",
                "D: Jerusalem",
                "B"]

for i in range(0, len(question_one)-1):
    print(question_one[i])
answer = input("Please enter your answer: -> ")
if answer == question_one[-1]:
    print("all good")
else:
    print("incorrect")



