

#loop needed

# create function

def get_user_input(m):
    getting_input = True
    while getting_input == True:
        try:
            user_input=int(input(m))
        except ValueError:
            print("You have not entered a whole number")
            # jump to top of loop
            continue
        if user_input < 1 or user_input > 10:
            print("You have not entered a number between 1 and 10")
            continue
        # if we get to here, we have an appropriate input
        getting_input = False
    return user_input

balance = get_user_input("Please enter a balance value between 1 and 10  $")
print(balance)
