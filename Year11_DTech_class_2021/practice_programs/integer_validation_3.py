total_money = 0
def get_integer_input():
    # access total_money
    global total_money
    # set condition for loop
    have_correct_value = False
    # start the loop
    while have_correct_value == False:
        try:
            user_input = int(input("Please enter a number between 1 and 10: "))
        except ValueError:
            print("You have not entered an integer")
            #jump to top of loop to ask for entry again
            continue
        total_money = user_input
        #have the correct value so end loop
        have_correct_value = True

    

#call function
get_integer_input()
print("You entered {}".format(total_money))
