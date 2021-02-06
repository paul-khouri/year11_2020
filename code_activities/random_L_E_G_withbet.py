import random
lower = 4
higher = 15

#print(middle_number)
#print(my_random)

total_money = 0
run_game = True
while run_game == True:
    my_random = random.randint(lower,higher)
    middle_number = round((lower + higher)/2)
    print("A random number has been chosen between {} and {}".format(lower, higher))
    print(40*"-")
    print("Enter L if you think the number is less than {0} \n"
                "Enter G if you think the number is more than {0} \n"
                "Enter E if you think the number is equal to {0} : ".format(middle_number)  ) 


    guess = input("Enter your choice: -> ")
    print()
    bet = float( input("How much do you want to bet that you are correct?  $") )

    win = False
    if guess == "L" and my_random < middle_number:
        win = True
    elif guess == "G" and my_random > middle_number:
      win = True
    elif guess == "E" and my_random == middle_number:
      win = True
    elif guess != "G" and guess != "L" and guess != "E":
      print("you have not entered an appropriate letter")
      win = ""

    if win == True:
        print("You win")
        total_money += bet
    elif win == False:
        print("You Lose")
        total_money -= bet
    else:
        print("No outcome")

    print("The number was {}".format(my_random))
    print("Your total is {:.2f}".format(total_money))

    play_again = input("Would you like to play again (Enter Y or N)?  -> ")
    if play_again == "N":
        run_game = False
    print("_"*50)


print("Program has ended")
        
    



