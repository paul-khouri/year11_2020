

def get_user_input(m):
    getting_input = True
    while getting_input == True:
        try:
            user_input = int(input(m))
        except ValueError:
            print("You have not entered a whole number")
            continue
        if user_input<1 or user_input >10:
            print("Your value is not between 1 and 10")
            continue
        getting_input = False
    return user_input


balance = get_user_input("Please enter a balance amount between $1.00 and $10.00.  $ ")
print("Your balance is ${:.2f}".format(balance))
        
