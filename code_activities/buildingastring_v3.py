import random

my_list=["c", "o", "f", "e"]

string_list = []

counter = 0
while counter < 1000:
    my_string = ""
    count = 1
    while True:
        my_letter = random.choice(my_list)
        my_string += my_letter
        #print(my_letter)
        if my_string.count("c")>=1 and my_string.count("o")>=1 \
           and my_string.count("f")>=2 and my_string.count("e")>=2:
            break
        count += 1
    string_list.append(my_string)
    counter += 1
    # print(my_string)
#print(string_list)
string_list.sort(key=len)
print(string_list[0])
print(string_list[- 1])

total_times = 0
number_trials = 0
for x in string_list:
    total_times += len(x)
    number_trials += 1
print(total_times)
print(number_trials)
    


