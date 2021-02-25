# using a "continue " condition
cont = "Y"
while cont =="Y":
    print("We are inside the loop")
    user_input=input("Please enter Yes to stay in the loop")
    # make the user input lower case
    user_input = user_input.lower()
    # test if the user DOES NOT enter Yes
    if user_input != "yes":
        cont = "N"
        print("This has stopped the loop")

print("We are now outside the loop")
  
        

