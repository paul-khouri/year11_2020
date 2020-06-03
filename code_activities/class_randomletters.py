import random

char_list = ["C", "O", "F", "E"]



C_count = 0
O_count = 0
F_count = 0
E_count = 0

char_string = ""
while True:
    my_char = random.choice(char_list)
    char_string += my_char
    # count number of C, O, 
    C_count = char_string.count("C")
    O_count = char_string.count("O")
    F_count = char_string.count("F")
    E_count = char_string.count("E")
    if C_count >= 1 and O_count >= 1 and F_count >= 2 and E_count >= 2:
        break
    # increment count

    
print(char_string)
print( len(char_string) )

#print(char_string.count("C"))
