Q_ONE = {
    "question": "What is the capital of France -> ",
    "answer": "Paris"
    }

Q_TWO = {
    "question": "What is the capital of Russia -> ",
    "answer": "Moscow"
    }

Q_THREE = {
    "question": "What is the capital of Japan -> ",
    "answer": "Tokyo"
    }

Q_FOUR = {
    "question": "What is the capital of Australia -> ",
    "answer": "Canberra"
    }
print("Quiz starts now")
user_answer = input(Q_ONE["question"])
if user_answer==Q_ONE["answer"]:
    print("Great work")
else:
    print("Better luck next time")

user_answer = input(Q_TWO["question"])
if user_answer==Q_TWO["answer"]:
    print("Great work")
else:
    print("Better luck next time")

user_answer = input(Q_THREE["question"])
if user_answer==Q_THREE["answer"]:
    print("Great work")
else:
    print("Better luck next time")

user_answer = input(Q_FOUR["question"])
if user_answer==Q_FOUR["answer"]:
    print("Great work")
else:
    print("Better luck next time")
