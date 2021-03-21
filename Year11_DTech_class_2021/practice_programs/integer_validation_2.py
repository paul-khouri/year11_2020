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
    #have the correct value so end loop
    have_correct_value = True

print("You entered {}".format(user_input))
