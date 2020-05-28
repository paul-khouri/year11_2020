question_one = {
    "question": "What is the capital of France?",
    "A": "Paris",
    "B": "Moscow",
    "C": "Shanghai",
    "answer": "C"
    }
print(question_one["A"])
print(question_one["B"])
print("-"*30)

for x,y in question_one.items():
    if x in ["A", "B", "C"]:
        print("{} , {}".format(x,y))
