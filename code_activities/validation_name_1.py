chars = ["a","b","c","d","e","f","g","h","i","j"," k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", " ", "-"]
have_name = False
while have_name == False:
    
    name = input("Please enter your name: -> ")
    # check name lenght and continue to the top
    if len(name)< 2 or len(name) > 20:
        print("This doesn't look like a valid name, please try again")
        continue
    # assume all the charcters are acceptable
    chars_okay = True
    # loop through the letters in the name (that have been set to lower case)
    for x in name.lower():
        # if an unacceptable character is found
        # print a useful message
        # set chars_okay to be false
        if x not in chars:
            print("{} is not an acceptable character in a name.".format(x))
            chars_okay = False
    # once the lettter loop is finished
    # check if chars_okay is false and if it is
    # continue to top of loop
    if chars_okay == False:
        continue

    # if no problems
    have_name = True

print("Welome {}".format(name.title()))
    
    
