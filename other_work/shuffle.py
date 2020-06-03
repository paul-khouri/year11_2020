import random

my_array = []
for i in range(0,20):
    my_array.append(i)
print(my_array)


def shuffle(L):
    for i in range(0, 1000):
        i_one = random.randint(0, len(L)-1)
        i_two = random.randint(0, len(L)-1)
        temp = L[i_one]
        L[i_one] = L[i_two]
        L[i_two] = temp
    return L
    

#my_array=shuffle(my_array)
random.shuffle(my_array)
print(my_array)
