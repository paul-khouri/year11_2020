age = 18

if age >= 18:
    print("You are an adult")
else:
    print("you are still a minor")
print(20*"-")

if age > 18:
    print("You are an adult")
elif age == 18:
    print("This is your first year as an adult")
else:
    print("you are still a minor")
print(20*"-")

# True False (booleans)
flour = False
sugar = True
#grams (integer) 
butter = 200

# nesting 
if flour:
    if sugar:
        print("You have flour and sugar")
    else:
        print("You have flour but no sugar")     
elif sugar:
    print("You have sugar but no flour")
else:
    print("Nothing in the cupboard")
print(20*"-")

# and or
if flour or sugar:
    if butter > 250:
        print("You should be able to make something")
    else:
        print("Low on butter")
else:
    print("Out of dry ingredients")   
print(20*"-") 








    
    
    


    
