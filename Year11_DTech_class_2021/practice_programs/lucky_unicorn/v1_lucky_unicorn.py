import random
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
player_amount=int(input("Please enter a value between 1 and 10: -> "))
print("You have entered ${:.2f}".format(player_amount))
#game play

player_token = random.choice(tokens)
#deduct $1
player_amount -= 1
#evaluate result based on which tken has been generated
if player_token == "unicorn":
    player_amount += 5
    print("Congratulations, you had a {}".format(player_token)) 
elif player_token == "horse" or player_token == "zebra":
    player_amount +=0.5
    print("You had a {}".format(player_token)) 
else:
    print("Unfortunately you had a {}".format(player_token))
print("Your balance is now ${:.2f}".format(player_amount))

