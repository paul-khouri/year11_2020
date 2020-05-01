def run_question(Q):
    user_answer = input(Q["question"])
    if user_answer==Q["answer"]:
        print("Great work")
    else:
        print("Better luck next time")
    
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

Q_FIVE = {
    "question": "What is the capital of Thailand -> ",
    "answer": "Bangkok"
    }

GAME_QS = [Q_ONE, Q_TWO, Q_THREE, Q_FOUR, Q_FIVE]
         

#print(GAME_QS[1]["question"])
#print(len(GAME_QS))

counter = 0
while counter < len(GAME_QS):
    run_question(GAME_QS[counter])
    counter += 1


















#GAME_QS = [Q_ONE,Q_TWO,Q_THREE,Q_FOUR]


#print(GAME_QS[0]["question"])
#print(GAME_QS[1]["question"])
#print(len(GAME_QS))
#counter = 0
#while counter<len(GAME_QS):
#    run_question(GAME_QS[counter])
#    counter += 1




