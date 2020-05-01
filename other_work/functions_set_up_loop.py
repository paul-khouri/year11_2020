# loop to add up consecutive numbers , up to and including 10
# 1+ 2+ 3+ 4 + ... + 10

count = 1
my_sum = 0
while count <= 10:
    my_sum = my_sum + count
    count += 1
#print(my_sum)

# define a function
def my_addition():
    count = 1
    my_sum = 0
    while count <= 10:
        my_sum = my_sum + count
        count += 1
    print(my_sum)

# call a function
my_addition()
my_addition()
my_addition()
my_addition()
    
