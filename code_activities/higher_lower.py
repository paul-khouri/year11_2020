import random

mainLoop="y"
while mainLoop=="y":
    #declare variables
    name=""
    secretNumber=0
    guess=0
    count=0
    min_num = 1
    max_num = 100
    #get user input and validate
    getUserNameLoop="y"
    while getUserNameLoop=="y":
        name=input("Please enter your name: ")
        if len(name)<2 or len(name)>30 or name.isalpha()!=True:
            print("Please enter a valid name")
            continue
        else:
            #name has been captured correctly
            getUserNameLoop="n"
    # welcome
    print("Hello {}, you are about to play a guessing game".format(name))
    print("where you need to guess the secret number between {} and {}".format(min_num, max_num))
    secretNumber=random.randint(min_num,max_num)
    #testing help
    #print("Testing help: the secret number is {}".format(secretNumber))
    ready=input("Press enter to start  ")
    #start game
    gameLoop="y"
    while gameLoop=="y":
        # get guess and validate
        getGuessInputLoop="y"
        while getGuessInputLoop=="y":
            try:
                guess=int(input("Please guess the secret number between {} and {}  ".format(min_num, max_num)))
            except ValueError:
                print("Please enter a valid integer")
                continue
            if guess<min_num or guess>max_num:
                print("Please enter a number between 1 and 50".format(min_num, max_num))
            else:
                # integer correctly entered
                getGuessInputLoop="n"
        #guess count
        count=count+1
        #respond to input
        if guess<secretNumber:
            print("Your guess is too small")
        elif guess>secretNumber:
            print("Your guess is too large")
        else:
            #number is found, end loop and print responses
            print("You have found it!!")
            gameLoop="n"
            print("You took {} tries to find it".format(count))
            if count<5:
                print("You are really fast")
            elif count<7:
                print("Pretty good")
            else:
                print("You can improve, I think")
    #exited game loop
    mainLoop=input("Do you want to play again?  y/n     ")
#exited main loop
print("The program has ended")
