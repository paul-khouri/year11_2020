# roll a dice
import random
two_d_list = []


    
def searchfor(n):
    if len(two_d_list)== 0:
        two_d_list.append([n,1])
        return
    added = False
    for sublist in two_d_list:
        if sublist[0]==n:
            sublist[1] += 1
            added = True
            break
    if added == False:
        two_d_list.append([n,1])
        
for i in range(0,1500):
    diceroll = random.randint(1,6)+random.randint(1,6)+random.randint(1,6)
    searchfor(diceroll)
    #print(diceroll)


two_d_list.sort()
print(two_d_list)
        
