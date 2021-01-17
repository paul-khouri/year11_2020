my_class = ["Agatha" ,"Melinda", "Harriet", "Hine", "Dandelion" , "Te Aroha"]

#print out a name at a specific index (use the square bracket notation)
# this prints out the fourth person in the last
print(my_class[3])
print()
# print the list out "informally"
print(my_class)
print()
# print using a loop (this is the usual way to do it)
# this a shorthand way of doing it,
# where the "x" is, we can use anything we like and it
# will hold the value on each iteration of the loop
for x in my_class:
    print(x)
print()
# find out how long the list is (you often need to do this)
class_length = len(my_class)
output = "There are {} students in the class\n".format(class_length)
print(output)
# sort the list
my_class.sort()
print(my_class)
print()
# shuffle the list
# for this we need the random module(should be up the top)
import random
random.shuffle(my_class)
print(my_class)
print()
# add a new name to a list
my_class.append("Phoebe")
print(my_class)
print()
# check if someone is in the list
check_name = "Jane"
if check_name in my_class:
    print("{} is in the class".format(check_name))
else:
    print("{} is not in the class".format(check_name))
print()
# find the index number of a particular name (where is Harriet??)
index_num = my_class.index("Harriet")
print("{} is at index number {}".format("Harriet" , index_num))
print()
# remove someone from the list
my_class.remove("Harriet")
print(my_class)
print("{} is no longer in the list".format("Harriet"))



