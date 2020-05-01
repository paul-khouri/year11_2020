import random

def get_user_input(m):
    '''takes string message as argument
    and ensures user input is an integer between 1 and 10
    returns user input
    '''
    getting_input = True
    while getting_input == True:
        try:
            user_input = int(input(m))
        except ValueError:
            print("You have not entered a whole number")
            continue
        if user_input<1 or user_input >10:
            print("Your value is not between 1 and 10")
            continue
        getting_input = False
    return user_input

# print output for start of Lucky Unicorn Game
print("------ Welcome to the Lucky Unicorn Game ---------")
print("Enter between $1 and $10 to play")
print("It costs $1 per round")
print("If you get a unicorn you will get $5 back")
print("If it is a Zebra or Horse you get 50c back")
print("A donkey gives nothing back")
print("------ Start -------------------------------------")
print()
# get amount of money to play with
tokens = ["horse", "zebra" , "donkey", "unicorn"]
player_amount = get_user_input("Please enter a balance amount between $1.00 and $10.00.  $ ")
print("Your balance is ${:.2f}".format(player_amount))
#game play
play=""
while play=="":
    player_token = random.choice(tokens)
    player_amount -= 1
    if player_token == "unicorn":
        player_amount += 5
        print("Congratulations, you had a {}".format(player_token)) 
    elif player_token == "horse" or player_token == "zebra":
        player_amount +=0.5
        print("You had a {}".format(player_token)) 
    else:
        print("Unfortunately you had a {}".format(player_token))
    print("Your balance is now ${:.2f}".format(player_amount))
    if player_amount < 1:
        print("Unfortunately you do not have enough to play any further")
        play = "q"
    else:
        play=input("Press <Enter> to continue or quit(q)")
print("Thank you for playing")
