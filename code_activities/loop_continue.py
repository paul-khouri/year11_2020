continue_program = True
while continue_program == True:
    print("This where the program runs")
    # as if user wants to run the program (or part of it) again
    user_response = input("Would you like to play again? (Y/N) - >  ")
    if user_response == "Y":
        print("Here we go again")
    elif user_response == "N":
        print("Thankyou for playing")
        continue_program = False
    else:
        print("Your input was not recognised (and we should do something about this)")

print("The program has ended")
                          
