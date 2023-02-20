# a hash makes a comment (this is not read by the program)
# so we can explain what we are doing


# create two integer variables
num_one = 45
num_two = 380

# create two string variables
str_one = "60"
str_two = "Good morning "

print(num_one + num_two)
print(num_one - num_two)
print(num_one * num_two)
print(num_one / num_two)

output="${:.2f}".format(round(num_one / num_two, 2))
print(output)

print(str_one + str_two)
#print(str_two * num_two)
print("-"*200)


