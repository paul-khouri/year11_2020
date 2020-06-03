#next trial
#number     Three
#whats good= it works: more efficient than 2
#whats bad= would be better if it was more helpful to the user
#it would be good if it accepts lower case letters

def check_user_input_trial_three():
     # this needed to be spelt correctly
    getting_some_input = True
    # you needed a semi colon after the ==True
    while getting_some_input ==True:
         #everything below becomes indented
         user_input = input("please enter your choice: ")
    #change the user input to upper case
         user_input = user_input.upper()
         if user_input in [ "A", "B", "C", "D" ]:
             return user_input
         else:
             print(" your choice is not an option i can understand")
             print("Please enter: only capital  A , B , C  or D")
             continue
# make sute the function name here is the same as it is written above
#(you had a capital T above)
answer = check_user_input_trial_three()
print(answer)
