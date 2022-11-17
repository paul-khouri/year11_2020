import random

#declare variables
name=""
secret_number=0
guess=0
count=0
MIN_NUM = 1
MAX_NUM = 100

#get user input and validate
name=input("Please enter your name: ")
# welcome
print("Hello {}, you are about to play a guessing game".format(name))
print("where you need to guess the secret number between {} and {}".format(MIN_NUM,MAX_NUM))

mainLoop="y"
while mainLoop=="y":
    #generate secret number
    secret_number=random.randint(MIN_NUM,MAX_NUM)
    #testing help
    #print("Testing help: the secret number is {}".format(secretNumber))
    ready=input("Starting new game, press enter:")
    #--------   start game
    # reset count
    count=0
    question_loop="y"
    while question_loop =="y":
        guess=int( input("Please guess the secret number between {} and {}: ".format(MIN_NUM, MAX_NUM) ) )
        #respond to input
        if guess<secret_number:
            print("Your guess is too small")
        elif guess>secret_number:
            print("Your guess is too large")
        elif guess == secret_number:
            #number is found, end loop and print responses
            print("You have found it!!")
            question_loop ="n"
        else:
            print("Program error")
        # add to question count
        count=count+1
    # ----------  end of loop
    
    print("You took {} tries to find it".format(count))
    if count<5:
        print("You are really fast")
    elif count<7:
        print("Pretty good")
    else:
        print("You can improve, I think")
    mainLoop=input("Do you want to play again?  (y/n): ")
#----  exited main loop
print("Thankyou for playing")
print("The program has ended")
