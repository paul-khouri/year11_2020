hamburger_price = 7.5

try:
    num_burgers = int(input("How many hamburgers would you like? -> "))
except ValueError:
    print("The entry is not a valid integer")

#total_cost = num_burgers*hamburger_price
#print("Please pay ${:.2f}".format(total_cost))
