Q= "six"
A="ono"

def validate_answer(m):

    #start loop to validate user entry
    getting_answer = True
    while getting_answer == True:
        
        # get input and make lower case
        user_input= input(m)
        user_input = user_input.lower()
        
        # we want an input between 2 and 15 characters
        if len(user_input) < 2 or len(user_input)>15:
            print("You don't seem to have entered a valid answer, please try again")
        else:
            return user_input
            getting_answer = False


message = "What is the Māori word for {}: ".format(Q)
user_input = validate_answer(message)
                             
if user_input == A:
    print("Great")
else:
    print("Unfortunately you are incorrect")
