
# getting user input
# all user input is cast a string data type
user_input = input("Please enter your name")
print(type(user_input))
# if we want to change the datatype from the input
# we need to cast to a new data type
user_input = int( input("Please enter a number") )
print(type(user_input))
