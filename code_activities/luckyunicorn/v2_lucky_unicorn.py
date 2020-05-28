import random
error_int = "Please enter an integer value"
error_amount = "You value was either too high or too low"

def getInput(m, low, high):
    value = False
    while value == False:
        try:
            player_amount = int(input(m))
        except ValueError:
            print(error_int)
            continue
        if player_amount < low or player_amount > high:
            print(error_amount)
            continue
        return player_amount
            
        

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
tokens = ["horse", "horse","zebra", "horse","zebra","zebra" , "donkey","donkey", "unicorn"]
# values for each token
COST = 1
UNICORN = 5
ZEBRA = 0.5
DONKEY = 0
HORSE = 0.5

player_amount= getInput("Please enter a value between 1 and 10: -> " , 1 ,10)
print("You have entered ${:.2f}".format(player_amount))
#game play
play=input("Press <Enter> to continue or quit(q)")
while play=="":
    player_token = random.choice(tokens)
    player_amount -= 1
    if player_token == "unicorn":
        player_amount += 5*COST
        print("Congratulations, you had a {}".format(player_token)) 
    elif player_token == "horse" or player_token == "zebra":
        player_amount +=0.5*COST
        print("You had a {}".format(player_token)) 
    else:
        print("Unfortunately you had a {}".format(player_token))
    print("Your balance is now ${:.2f}".format(player_amount))
    if player_amount < COST:
        print("Unfortunately you do not have enough to play any further")
        play = "q"
    else:
        play=input("Press <Enter> to continue or quit(q)")
print("Thank you for playing")
