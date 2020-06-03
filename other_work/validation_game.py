# function up near top of code
def get_single_input():
    get_input = True
    while get_input == True:
        user_input = input("Please enter A,B,C or D  ")
        user_input = user_input.strip()
        user_input = user_input.upper()
       
        #-----
        if len(user_input) != 1:
            print("You need to enter only one character")
            continue
        if user_input not in ["A","B","C", "D"]:
            print("You have not entered A or B or C or D")
            continue
        get_input = False
        # if we get this far we should have what we want
        return user_input
    
        

# you game code
# somewhere you request user input

user_answer = get_single_input()
print(user_answer)
if user_answer == "A":
    print("You got it right")
else:
    print("Incorrect answer")
