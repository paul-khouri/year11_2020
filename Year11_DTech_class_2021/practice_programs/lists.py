# create a list , each item is separated by commas
class_list=["Adia","Ruby", "Emily", "Joyce", "Gertrude"]
#index:          0           1            2               3               4

#access a particular item at an index number
print(class_list[0])
print(class_list[4])
#python trick (access the last item)
print(class_list[-1])

# find how long the list is (it will be 5, but its last index number is 4)
print(len(class_list))
# add someone to the list
class_list.append("Bianca")
# a basic print out to see what the list has in it
print(class_list)

# use a for loop to print out each item in the list
# the i is a counter 
for i in range(0,len(class_list)):
    output="index {} is {}".format(i, class_list[i])
    print(output)

#get a name from the user and add it (append it) to the list
newbie=input("please enter a new memeber for the class:")
class_list.append(newbie)
#get a name from the user 
check_person=input("enter a name to see if they are in the class:")
# find out if that name is in the list
if check_person in class_list:
    output=("{} is in the class").format(check_person)
else:
    output="{} is not in the class".format(check_person)

print(output)

# sort the list in alpabetical order
class_list.sort()
# print out again, nicely
for i in range(0,len(class_list)):
    output="index {} is {}".format(i, class_list[i])
    print(output)
# remove a person from the list
out_person=input("who would you like to expel")
class_list.remove(out_person)
#do a qick check to see that they have been removed
print(class_list)

