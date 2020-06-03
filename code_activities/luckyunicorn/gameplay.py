# testing game play
player_amount = 5
player_token = "horse"
player_amount -= 1
if player_token == "unicorn":
    player_amount += 5
    print("Congratulations, you had a {}".format(player_token)) 
elif player_token == "horse" or player_token == "zebra":
    player_amount +=0.5
    print("You had a {}".format(player_token)) 
else:
    print("Unfortunately you had a {}".format(player_token))
print("Your balance is now {:.2f}".format(player_amount))
