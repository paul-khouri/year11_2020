Q= "six"
A="ono"


message = "What is the Māori word for {}".format(Q)
user_input= input(message)
user_input = user_input.lower()
                               
if user_input == A:
    print("Great")
else:
    print("Unfortunately you are incorrect")
