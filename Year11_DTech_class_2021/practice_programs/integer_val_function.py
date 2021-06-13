user_input = 0 
def get_integer_input():
    global user_input
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
        if user_input < 1:
            print("You number is less than 1")
            continue
        elif user_input > 10:
            print("You number is more than 10")
            continue
        #have the correct value so end loop
        have_correct_value = True

#call function
get_integer_input()
print("You entered {}".format(user_input))
    
    
