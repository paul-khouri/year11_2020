# adding up consecutive numbers 1 + 2 + 3+ ...

# defining a function
def my_addition(n):
    count = 1
    my_sum = 0
    while count <= n:
        my_sum = my_sum + count
        count += 1
    return my_sum

my_add = my_addition(10000)

print(my_add)
my_add = my_addition(99945)
print(my_add)
