import random
def print_pic(n):
    a= "{0:_<12}{1:_^3}".format("|", "")
    b= "{0:<12}{1:^3}".format("|", "|")
    c= "{0:<12}{1:^3}".format("|", "|")
    d= "{0:<12}{1:^3}".format("|", "0")
    e= "{0:<12}{1:^3}".format("|", "-|-")
    f= "{0:<12}{1:^3}".format("|", "/ \\")
    g= "{0:_<12}{1:_^3}".format("|", "")
    pic_set = [a,b,c,d,e,f,g]
    if n > len(pic_set):
        n = len(pic_set)
    for i in range(0,n):
        print(pic_set[i])
    print()
    if n == len(pic_set):
        return True
    else:
        return False

#def get_lower_case_one_char():
    


def play_round(w):
    error_count = 0
    selected_letters = []
    word = list(w)
    current_choice = ""
    game_over = False
    game_ended = False
    #start
    for i in range(0, len(w)):
        print(" _ ", end="")
    print()
    while game_ended == False:
        current_choice = input("Please choose a letter: ->  ")
        print()
        if current_choice in word:
            if current_choice in selected_letters:
                print("You have already found that letter")
            else:
                selected_letters.append(current_choice)
                print("Yes, you got one!")
        else:
            error_count += 1
            game_over = print_pic(error_count)
            print("Sorry that letter is not in the word")
        print()
        if not game_over:
            found = True
            for i in range(0, len(word)):
                if word[i] in selected_letters:
                    print(word[i], end="")
                else:
                    found = False
                    print(" _ ", end="")
            if found == True:
                print()
                print("Congratulations you found it!")
                game_ended = True
        else:
            print( "Sorry, the hangman has got you :(" )
            game_ended = True
        print()
        print()

word_list = ["insane", "heaven", "typhoon", "tropical", "clemency"]
#randomly select word and place in current word list
count = 0
while count < 2:
    output = "Welcome to hangman"
    print(output)
    output = "Find the mystery word by choosing letters!"
    print(output)
    selected_word = random.choice(word_list)
    output = "Your word is {} letters long".format(len(selected_word))
    temp = input("Press enter to start")
    #print(selected_word)
    play_round(selected_word)
    count += 1




        

