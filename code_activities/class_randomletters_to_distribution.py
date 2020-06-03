import random

char_list = ["C", "O", "F", "E"]

string_list = []


def run_trial():
    counter  = 1
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
        counter += 1
    #print(char_string)
    return len(char_string)




total_trials = 1000000
trials = 1
total_chars = 0
while trials <= total_trials:
    total_chars += run_trial()
    trials += 1

    
print(total_chars)
print(total_trials)
my_average = total_chars/total_trials
print(my_average)

#print(string_list)
string_list.sort(key = len)
#print(string_list)
print(string_list[0])
print(string_list[-1])
print(len(string_list[0]))
print(len(string_list[-1]))

my_dict = {}
for i in range(len(string_list[0]), len(string_list[-1])+1 ):
    my_dict[i]=0
    #print(i)
    
#print(my_dict)
for x in string_list:
    my_dict[len(x)]+=1

print(my_dict)
my_sum = 0
for x in my_dict:
    my_sum += my_dict[x]
print(my_sum)
# dictionary not the same lenght as string list
for x,y in my_dict.items():
    temp = int(y)
    temp = temp/total_trials
    my_dict[x]= temp
print(my_dict)

my_file = open("distribution_next.txt","a")
for x,y in my_dict.items():
    my_string = "{},{:.6f}\n".format(x,y)
    my_file.write(my_string)
    
#my_file.write("hello")
#my_file.write("\n")
#my_file.write("goodbye")
my_file.close()
#my_file = open("MyFile.txt","w")
#my_file.write("")
#my_file.close()
    

               




    
