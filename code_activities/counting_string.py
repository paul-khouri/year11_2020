my_string = "woolloomooloo"

my_letters=[]
count_letters = []

for x in my_string:
    if x not in my_letters:
        my_letters.append(x)
        count_letters.append(my_string.count(x))

print(my_letters)
print(count_letters)
