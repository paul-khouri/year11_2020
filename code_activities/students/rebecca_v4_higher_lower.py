import random
import math


# choosing numbers



# get an integer from the user
def get_input(message, error,low):
    get_value = False
    while get_value == False:
        try:
            user_input = int(input(message))
        except ValueError:
            print(error)
            continue
        if  user_input <= low:
            print(error)
            continue
        elif user_input > low:
            get_value = True
            return user_input



                  




# game loop
start =""
while start=="":
    # all of these need to be inside the loop so they can be updated each time
    low = get_input("Please enter a low number: ", "Incorrect value", 0) 
    high = get_input("Please enter a number greater than {}: ".format(low), "Incorrect value", low)
    print("A random number has been chosen between {} and {}".format(low, high))
    print(30*"-")

    # generate randint
    my_random = random.randint(low,high)

    # generate number of guesses
    number = math.log(high-low,2)
    number = round(number)



    # get correct input
    count = number
    total_count = number
    print("You have {} attempts to guess the number".format(number))
    while count > 0:
        guess = get_input("Please enter a number between {} and {}: ->  ".format(low,high), "Incorrectvalue", low)
        count -= 1
        print(30*"*")
    
        # have guess and number, check and feedback
        if guess < my_random:
            print("Your guess is too low \n"
                  "Please try again")
        elif guess > my_random:
            print("Your guess is too high \n"
                  "Please try again")
        elif guess == my_random:
            print("You have guessed the right number!")
            break
        print("You have {} guesses left".format(count))
        
    # this only happens once the game has ended
    if count == 0:
        print("Sorry, you have ran out of guesses")

    else:
        print("You guess it in {} guesses".format(total_count-count))

    print("Thank you for playing")
    print(30*"_")  
    
    start = input("Press enter if you like to play again \n"
                  "Or the letter (q) if you want to quit: ")
