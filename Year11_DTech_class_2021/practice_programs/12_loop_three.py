continue_program = True
while continue_program == True:
    print("run some code here")
    user_input = input("Would you like to play again (Y/N) -> ")
    if user_input == "Y":
        print("Now playing again")
    elif user_input == "N":
        print("Thankyou for playing")
        # set program condition to false
        continue_program = False
    else:
        print("You input was not a valid entry")


print("The program has ended")
