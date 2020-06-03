from questions import get_questions

GAME_QS=get_questions() 
# a function to run a question take a dictionary as an argument
def run_question(Q):
     '''  takes the question dictionary
          checks user response
          returns none
     '''
     # get question key from dictionary and ask user to answer
    user_answer = input(Q["question"])
    # check user answer is same as answer key in dictionary
    if user_answer==Q["answer"]:
        print("Great work")
    elif user_answer == "q":
        return "q"
     # or print wrong answer message
    else:
        print("Better luck next time")
   


def main_game():
    counter = 0
    while counter<len(GAME_QS):
        result = run_question(GAME_QS[counter])
        if result == "q":
            return "q"
        counter += 1
    return None

   
def main():
    run_game = True
    while run_game == True:
        result = main_game()
        play_again = input("Do you want to play again (y/n)")
        if play_again != "y":
            print("Thankyou for playing")
            run_game = False

main()



        




