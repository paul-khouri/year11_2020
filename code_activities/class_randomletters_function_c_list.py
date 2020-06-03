import random

char_list = ["C", "O", "F", "E"]

# empty list
string_list = []


#----------------------------
def make_coffee():
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
            string_list.append(char_string)
            break
        # increment count

        
    #print(char_string)
    #print( len(char_string) )
    return len(char_string)
#--------------------------------


total_trials = 1000000
trials = 1

total_string_lengths = 0

while trials <= total_trials:
    my_number = make_coffee()
    total_string_lengths += my_number
    #print(my_number)
    trials +=1
#print(total_string_lengths)
average = round(total_string_lengths / total_trials)
print("On average you will need {} visits".format(average))
#print(string_list)

string_list.sort(key=len)
#print(string_list)
#print first item (thing)
print(string_list[0])
#print last item
print(string_list[total_trials-1])
print(   len( string_list[total_trials-1] ) )










#print(string_list)



#string_list.sort(key = len)



















