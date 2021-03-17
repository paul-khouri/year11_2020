total_money = 10
chosen_token = "Zebra"

total_money -= 1
if chosen_token == "Unicorn":
    total_money += 5
elif chosen_token == "Horse":
    total_money +=0.5
elif chosen_token == "Zebra":
    total_money +=0.5
elif chosen_token == "Donkey":
    total_money+=0

print("You got a {}".format(chosen_token))
print("You now have ${:.2f}".format(total_money))

