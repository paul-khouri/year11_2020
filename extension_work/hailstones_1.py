import matplotlib.pyplot as plt
import numpy as np


def createplot(t,s):
    fig, ax = plt.subplots()
    ax.plot(t,s)
    title = "Hailstone for {}".format(my_number)

    ax.set(xlabel='step', ylabel='value', title = title)
    ax.grid()

    fig.savefig("hs.png")
    plt.show()

def run_hailstone(my_number,plot_required):
    n = my_number
    if plot_required:
        s=np.array(my_number)

    c=0
    while n !=1:
        if n%2 == 1:
            n=3*n+1
        else:
            n= n/2
        if plot_required:
            s=np.append(s,int(n))
        c += 1

    if plot_required:
        t = np.arange(0,c+1, 1)
        createplot(t,s)
    return c
    
        
#my_number = 101
#plot_required = True
#run_hailstone(my_number, plot_required)


def create_stemplot(min_num, max_num):
    max_c = 0
    max_i = 0
    y = np.array([])
    for i in range(min_num,max_num+1):
        c = run_hailstone(i, False)
        y=np.append(y,int(c))
        if c >= max_c:
            max_c = c
            max_i = i
    print(max_i)
    print(max_c)
    x = np.linspace(min_num,max_num,num=max_num-min_num+1)
    print(x.size)
    print(y.size)
    fig, ax = plt.subplots()
    ax.stem(x,y)
    ax.set(xlim=(min_num-1, max_num+1), xticks=np.arange(min_num, max_num+1, step=10),
       ylim=(0, max_c+1), yticks=np.arange(0, max_c+1, step = 5))
    plt.grid(True)
    plt.show()
    print(x)
    print(y)

create_stemplot(2000,2100)






    
