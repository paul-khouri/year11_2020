# after the first trial of this idea
# I modified it to simplify the
# conditions so it is now mush more efficient

total_money = 10
chosen_token = "Unicorn"

total_money -= 1
if chosen_token == "Unicorn":
    total_money += 5
elif chosen_token == "Horse" or chosen_token == "Zebra":
    total_money +=0.5


print("You got a {}".format(chosen_token))
print("You now have ${:.2f}".format(total_money))

