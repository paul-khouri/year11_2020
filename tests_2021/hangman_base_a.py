selected_letters = []
word = ["B", "A", "N", "A", "N", "A"]
current_choice = ""
found = False
while found == False:
    current_choice = input("Please choose a letter: ")
    if current_choice in word:
        selected_letters.append(current_choice)
        
    found = True
    for i in range(0, len(word)):
        if word[i] in selected_letters:
            print(word[i], end="")
        else:
            found = False
            print("_", end="")
    print()
    

