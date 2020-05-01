
# function with an argument
def my_addition(n):
    start_count = 1
    count = start_count
    my_sum = 0
    my_string=""
    while count <= n:
        my_sum = my_sum + count
        if count == start_count:
            my_string="{}".format(count)
        else:
            my_string="{}+{}".format(my_string, count)
        count += 1
        
    my_string="{}={}".format(my_string, my_sum)
    print(my_sum)
    print(my_string)

my_addition(3)
my_addition(1)
