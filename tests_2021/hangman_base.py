word_letters =    ["j","a","z","z","y"]
answer_letters =["_","_","_","_","_"]
# user enters a letter and if it is correct, add it to the answer list
print(answer_letters)
letter_guess = input("Please choose a letter: -> ")
if letter_guess in word_letters:
    print("Yes you have guessed a letter")
    for i in range(0, len(word_letters)):
        if word_letters[i] == letter_guess:
            answer_letters[i] = letter_guess
else:
    print("Incorrect choice")
print(answer_letters)
        
    
    
