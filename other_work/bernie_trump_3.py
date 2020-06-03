



A={ "bernie": 2,
    "biden" :4,
    "trump": 1
    }
B={
    "bernie": 5,
    "biden" :2,
    "trump" : 0
    }

def updater(D, totals):
    for x, y in D.items():
        totals[x] += y


def main():
    totals={
    "bernie": 0,
    "biden" : 0,
    "trump" : 0
    }
    print(totals)
    updater(A, totals)
    updater(A, totals)
    updater(A, totals)
    print(totals)

main()
        
    
    
