import random

char_list = ["C", "O", "F", "E"]


chars_in_seven = 0

C_count = 0
O_count = 0
F_count = 0
E_count = 0


trials = 0
trial_total = 1000000
while trials < trial_total:
    counter  = 1
    char_string = ""
    while counter <= 7:
        my_char = random.choice(char_list)
        char_string += my_char
        # count number of C, O, F, E
        C_count = char_string.count("C")
        O_count = char_string.count("O")
        F_count = char_string.count("F")
        E_count = char_string.count("E")

        # increment count
        counter += 1
    # test string at end
    if C_count >= 1 and O_count >= 1 and F_count >= 2 and E_count >= 2:
        chars_in_seven +=1
    #print(char_string)
    trials += 1
    
print(chars_in_seven/trial_total)
#print(char_string.count("C"))
