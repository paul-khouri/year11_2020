bernie = 0
trump = 0
biden = 0

A={ "bernie": 2,
    "biden" :4,
    "trump": 1
    }
B={
    "bernie": 5,
    "biden" :2,
    "trump" : 0
    }
print(A)
def updater(D):
    global bernie
    global trump
    global biden
    for x, y in D.items():
        if x=="bernie":
            print(x)
            print(y)
            bernie += y
            print(bernie)
        elif x=="biden":
            biden += y
        else:
            trump +=y
output = "bernie {} ; trump {} ; biden {}".format(bernie, trump, biden)
print(output)
updater(A)
output = "bernie {} ; trump {} ; biden {}".format(bernie, trump, biden)
print(output)
        
    
    
