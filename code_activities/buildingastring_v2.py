import random

my_list=["c", "o", "f", "e"]

my_string = ""
count = 1
while count<100:
    my_letter = random.choice(my_list)
    my_string += my_letter
    #print(my_letter)
    if my_string.count("c")>=1 and my_string.count("o")>=1 \
       and my_string.count("f")>=2 and my_string.count("e")>=2:
        break
    count += 1
for x in my_list:
    print("{} * {}".format(x,my_string.count(x)))
print(my_string)
print("count is {}".format(count))

