question = "What is the capital of France?"
answers = ["A: Berlin", "B: Moscow", "C: Paris", "C"]
print(question)
for i in range(0, len(answers) - 1):
    print(answers[i])
user_answer = input("Please enter your choice: ")
if user_answer == answers[-1]:
    print("Great")
else:
    print("Incorrect")
