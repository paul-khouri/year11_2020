# temperature 
temp = int( input("What will be the maximum temperature today? ") )
if temp <10:
    print("Cold today")
elif temp < 20:
    print("Regular Wellington day, today")
else:
    print("Hot today")
print(20*"-")

# allowance
kitchen = input("Have you helped clean the kitchen (y/n) ? ")
allowance = 5
if kitchen == "y":
    allowance += 2
else:
    allowance +=1
output = "Your allowance is now ${:.2f} ".format(allowance)
print(output)
print(20*"-")

# allowance extended
kitchen = input("Have you helped clean the kitchen (y/n) ? ")
garbage = input("Have you helped put out the garbage (y/n) ? ")
allowance = 5

if kitchen == "y" and garbage == "y":
    allowance += 4
elif kitchen == "y" or garbage == "y":
    allowance += 2
else:
    allowance +=1
output = "Your allowance is now ${:.2f} ".format(allowance)
print(output)
print(20*"-")

# minimum number
a = int( input("Please enter a number: ") )
b = int( input("Please enter a number: ") )
c = int( input("Please enter a number: ") )

if a < b and a < c:
    print( "The minumum is {}".format(a) )
elif b < c:
    print( "The minumum is {}".format(b) )
else:
    print( "The minumum is {}".format(c) )
print(20*"-")
# university entrance
age = 17
ncea = True
english = True
# option 1
if english:
    if age > 20 or (age > 16 and ncea):
        print("Accepted")
    else:
        print("Not accepted")
else:
    print("Not accepted")
print(20*".")
# option 2
if english and ( age > 20 or (age > 16 and ncea)) :
    print("Accepted")
else:
    print("Not accepted")
    
    
    
    
