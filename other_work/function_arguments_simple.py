
# function with an argument
def my_addition(n):
    count = 1
    my_sum = 0
    while count <= n:
        my_sum = my_sum + count
        count += 1
    print(my_sum)

#my_addition(3)
#my_addition(1)

# function with an argument and a return value
def my_addition_ret(n):
    count = 1
    my_sum = 0
    while count <= n:
        my_sum = my_sum + count
        count += 1
    return my_sum

my_add = my_addition_ret(5)
print(my_add)
