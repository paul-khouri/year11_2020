totals={
    "bernie": 0,
    "biden" : 0,
    "trump" : 0
    }



A={ "bernie": 2,
    "biden" :4,
    "trump": 1
    }
B={
    "bernie": 5,
    "biden" :2,
    "trump" : 0
    }

def updater(D):
    for x, y in D.items():
        totals[x] += y


def main():    
    print(totals)
    updater(A)
    updater(A)
    updater(A)
    print(totals)

main()
        
    
    
