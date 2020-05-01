# each element in a list has an index number
# the index counting starts at 0
# so index 1 is Jade
# the length of the list is 8
# the index of the last element 7
my_list = ["Grace", "Jade", "Anita", "Becky", "Holly", "Eleanor", "Alisa", "Molley"]


# print the fourth item in the list
print( my_list[3] )
print( len( my_list ) )
# print last element
print( my_list[ len(my_list) - 1 ] )
#print( my_list[10] )
print()

# print out the list using a loop
i = 0
while i < len(my_list) :
    print( my_list[i], end="" )
    i += 1
