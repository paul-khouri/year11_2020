# set a loop variable
have_name = False

while have_name == False:
    # request name
    name = input("Please enter your name: -> ")
    
    # check the number of characters in the name and
    # print error message if it is outside of an acceptable range.
    # and continue to top of loop is it is
    if len(name)< 2 or len(name) > 20:
        print("This doesn't look like a valid name, please try again")
        continue
    
    # if have got here, then all okay so end loop
    have_name = True

print("Welome {}".format(name))
    
    
