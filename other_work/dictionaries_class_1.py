multi_q = {
    "question": "What is the capital of France? ",
    "A" : "Paris",
    "B" : "Moscow",
    "C" : "Shanghai",
    "answer" : "A"
    }

# running a question
print(multi_q["question"])

# loop through the options
for x, y in multi_q.items():
    if x in ["A", "B", "C"]:
        print("{} . {}".format(x,y))
    
#request user answer
user_input= input("Please choose your answer")

