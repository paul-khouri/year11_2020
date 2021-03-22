import random

# declare variable to hold the amount of money the player is playing with
player_amount = 0
# define function to get user input and ensure their input is valid
# if not, the user will be asked again
def get_integer_input():
    # access total_money
    global player_amount
    # set condition for loop
    have_correct_value = False
    # start the loop
    while have_correct_value == False:
        try:
            user_input = int(input("Please enter a number between 1 and 10: "))
        except ValueError:
            print("You have not entered an integer")
            #jump to top of loop to ask for entry again
            continue
        player_amount = user_input
        #have the correct value so end loop
        have_correct_value = True


# print output for start of Lucky Unicorn Game
print("------ Welcome to the Lucky Unicorn Game ---------")
print("Enter between $1 and $10 to play")
print("It costs $1 per round")
print("If you get a unicorn you will get $5 back")
print("If it is a Zebra or Horse you get 50c back")
print("A donkey gives nothing back")
print("------ Start -------------------------------------")
print()

#list of tokens
tokens = ["horse","zebra","donkey", "unicorn"]


# get amount of money to play with
# by calling the get_integer_input function
get_integer_input()
print("You have entered ${:.2f}".format(player_amount))
print("------------------------- let's go!---------------------")
#game play
play=input("Press <Enter> to start")
# start the game loop
continue_program = True
while continue_program == True:
    # randomly select a token
    player_token = random.choice(tokens)
    # deduct $1 from the player_amount
    player_amount -= 1
    # respond depending on which tken has been selected
    if player_token == "unicorn":
        player_amount += 5
        print("Congratulations, you had a {}".format(player_token)) 
    elif player_token == "horse" or player_token == "zebra":
        player_amount +=0.5
        print("You had a {}".format(player_token)) 
    else:
        print("Unfortunately you had a {}".format(player_token))
    print("Your balance is now ${:.2f}".format(player_amount))
    # check if player has enough money
    if player_amount < 1:
        #if not end the game
        print("Unfortunately you do not have enough to play any further")
        continue_program = False
    else:
        # if they do, ask if they want to play again and end loop if they choose to quit
        user_input=input("Press <Enter> to continue or quit(q)")
        if user_input == "":
            print("Playing another round")
        elif user_input == "q":
            continue_program = False
            print("Ending game")
        else:
            print("Not sure, so let's play another round")
#loop has finished. print final message          
print("Thank you for playing")
