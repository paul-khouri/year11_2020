word_letters =    ["k","a","u","r","i"]
answer_letters =["_","_","_","_","_"]
# user enters a letter and if it is correct, add it to the answer list
letter_guess = input("Please choose a letter: -> ")
if letter_guess in word_letters:
    print("Yes you have guessed a letter")
    for i in range(0, len(word_letters)):
        if word_letters[i] == letter_guess:
            answer_letters[i] = letter_guess
else:
    print("Incorrect choice")
print(answer_letters)
        
    
    
