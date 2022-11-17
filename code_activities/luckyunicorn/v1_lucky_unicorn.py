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

# validation
# every user entry must be checked.
getting_money = True

while getting_money == True:
    try:
        player_amount=int(input("Please enter a value between 1 and 10: -> "))
    except ValueError:
        print("You have not entered a number, please try again")
        # go immediately to the top of the loop
        continue


    #test if money is not to large or small
    if player_amount < 1 or player_amount > 10:
        print("The money you have entered is too large or too small")
        continue
    else:
        getting_money= False


    




player_amount =10

print("You have entered ${:.2f}".format(player_amount))
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
    play=input("Press <Enter> to continue or quit(q)")
