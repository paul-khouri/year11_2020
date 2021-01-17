import random
total_money = 10
token_list = ["unicorn", "horse", "zebra", "donkey"]
values = [5, 0.5, 0.5, 0]
token_index = 3

total_money -=1
total_money +=values[token_index]


print("You got a {}".format(token_list[token_index]))
print("You now have ${:.2f}".format(total_money))

