hamburger_price = 7.5
#note the casting int(    ----   )
#this converts the string input to an integer
num_burgers = int(input("How many hamburgers would you like? -> "))

total_cost = num_burgers*hamburger_price
print("Please pay ${:.2f}".format(total_cost))
