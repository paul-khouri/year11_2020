# what's good?? It does the job
# the user cannot move on until
# they enter something acceptable
# what's bad about it?? Repeats itself
# alot. Difficult if we want to change it.
# Not very efficient

# this a trial ( our first option )
def check_user_input_trial():
     get_user_input = True
     while get_user_input == True:
          user_choice = input("please enter your choice: ")
          if user_choice == "A":
               return user_choice
          elif user_choice == "B":
               return user_choice
          elif user_choice == "C":
               return user_choice
          elif user_choice == "D":
               return user_choice
          else:
               print("Please enter A, B, C, D")
               continue
          
#answer = check_user_input_trial()
#print(answer)

# next trial
# what's good?? It works
# what's better?? More efficient, no repetition
# what's bad ?? Would be nice if we
# could be more helpful to the user.
# 
def check_user_input_trial_two():
     getting_some_input = True
     while getting_some_input == True:
          user_input = input("Please enter your choice: ")
          if user_input in ["A","B", "C", "D"]:
               return user_input
          else:
               print(" Your choice is not an option I can understand")
               print("Please enter only capital A, B, C, D")
               continue


#answer =check_user_input_trial_two()
#print(answer)

# it would be good if it accepted lower case
# letters
# run a little test useing lower case letters.
def check_user_input_trial_three():
     getting_some_input = True
     while getting_some_input == True:
          user_input = input("Please enter your choice: ")
          # change the user input to upper case
          user_input = user_input.upper()
          if user_input in ["A","B", "C", "D"]:
               return user_input
          else:
               print(" Your choice is not an option I can understand")
               print("Please enter only A, B, C or D")
               continue


answer =check_user_input_trial_three()
print(answer)

















     
