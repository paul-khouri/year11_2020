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
tokens_one = ["horse", "zebra" , "donkey", "unicorn"]
tokens_two = ["horse", "horse","zebra","zebra" , "donkey", "unicorn"]
tokens_three = ["horse", "horse","zebra","zebra" , "donkey","donkey", "unicorn"]
tokens_four = ["horse", "horse","zebra", "horse","zebra","zebra" , "donkey","donkey", "unicorn"]
tokens= tokens_two
player_amount=int(input("Please enter a value between 1 and 10: -> "))
start_amount = player_amount
print("You have entered ${:.2f}".format(player_amount))
#game play
play=""
count = 0
games_to_play = 1000000
while count < games_to_play:
    player_token = random.choice(tokens)
    player_amount -= 1
    if player_token == "unicorn":
        player_amount += 5
        #print("Congratulations, you had a {}".format(player_token)) 
    elif player_token == "horse" or player_token == "zebra":
        player_amount +=0.5
        #print("You had a {}".format(player_token)) 
    count += 1
    #play=input("Press <Enter> to continue or quit(q)")
print("Your balance is now ${:.2f}".format(player_amount))
average_pergame= (player_amount-start_amount)/games_to_play
print("Average win per game = ${:.2f}".format(average_pergame))
