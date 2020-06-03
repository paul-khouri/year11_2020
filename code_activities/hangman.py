word = "halloween"

def pic(c):
    if c >= 1:
        print(" "*30+"   _ _ _ _")
    if c >=2:
        print(" "*30+"   |     |")
    if c >=3:
        print(" "*30+"  ( )    |")
    if c >= 4:
        print(" "*30+"   |     |")
    if c >= 5:
        print(" "*30+"  ---    |")
        print(" "*30+"   |     |")
        print(" "*30+"  / \    |")
        print(" "*30+"       __|")
pic(5)
char_list = list(word)
char_individual_list=[]
char_list_chosen=[]

for x in char_list:
    if x not in char_individual_list:
        char_individual_list.append(x)

wrong_count = 0
while len(char_individual_list)>0:
    outstring = ""
    for x in char_list:
        if x in char_list_chosen:
            outstring += " "+x+" "
        else:
            outstring += " _ "
    print("{}\n\n".format(outstring))
    char = input("guess a letter: ")
    if char in char_individual_list:
        char_list_chosen.append(char)
        char_individual_list.remove(char)
    else:
        wrong_count += 1
        pic(wrong_count)
    if len(char_individual_list) == 0:
        print("you got it")
    

outstring = ""
for x in char_list:
    if x in char_list_chosen:
        outstring += " "+x+" "
    else:
        outstring += " _ "
print(outstring)

        
