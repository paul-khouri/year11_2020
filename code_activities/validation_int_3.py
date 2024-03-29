hamburger_price = 7.5
#set a condition for the loop
have_value = False
while have_value == False:
    try:
        num_burgers = int(input("How many hamburgers would you like? -> "))
    except ValueError:
        # a pleasant, helpful error message.
        print("Unfortunately you have not given a whole number for the hamburgers. Please try again")
        # introduce a 'continue', this means the program will jump straight back to the top of the loop.
        continue
    #if we get to this point then we have a valid integer, so end the loop
    have_value = True

# we now know that we have what we need, so can proceed
total_cost = num_burgers*hamburger_price
print("Please pay ${:.2f}".format(total_cost))
