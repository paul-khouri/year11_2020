# no commas
# check for clean print out

def read_file():
    E=[]
    M=[]
    my_file=open("Māori_Dictionary_Sheet.csv", mode="r")
    for line in my_file:
        #print(line, end="")
        line = line.replace("\n", "")
        line = line.strip()
        my_list = line.split(",")
        if(len(my_list) != 2):
            print("Problem")
            return None
        M.append(my_list[0].strip())
        E.append(my_list[1].strip())
        #print(my_list)
    return M, E
        

M, E =read_file()
print(M)
print(E)
    
