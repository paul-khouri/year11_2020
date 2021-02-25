age = 25
NCEA = True
English = False

if English == True:
    if age > 20:
        print("You can go")
    elif age >= 16 and NCEA == True:
        print("You can go")
    else:
        print("You cannot go")
else:
    print("You cannot go")
