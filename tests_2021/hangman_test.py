my_word = "kauri"
my_word_list = []
my_word_list[:0] = my_word
print(my_word_list)
# create answer list
answer_list = []
for x in my_word:
    answer_list.append("_")
print(answer_list)
temp_str = "   "
print(temp_str.join(answer_list))
while "_" in answer_list:
    guess = input("Please enter a letter")
    if guess in my_word_list:
        print("The letter is in the word")
        i = 0
        for x in my_word_list:
            if x == guess:
                answer_list[i] = guess
            i += 1
    else:
        print("The letter is not in the word")
    temp_str = "   "
    print(temp_str.join(answer_list))

