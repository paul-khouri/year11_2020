#initialise variables
my_name = "Harry"
my_age = 13
# print out variables in a sentence
my_output = "My name is {} and I am {} years old".format(my_name,my_age)
print(my_output)
# swap the order
my_output = "My name is {1} and I am {0} years old".format(my_name,my_age)
print(my_output)
# print the first one with 10 chararcter spaces centre aligned
# and the second one 10 character spaces right aligned
my_output = "My name is {:^10} and I am {:>10} years old".format(my_name,my_age)
print(my_output)
my_number = float(2.671998761726172)
print(my_number)
# print decimal to 4 decimal places (not rounded)
print("{:.4f}".format(my_number))
# print in 10 character spaces with trailing zeroes and with 2 decimal places
print("{:010.2f}".format(my_number))

      
