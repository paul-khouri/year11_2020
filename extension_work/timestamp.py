from datetime import datetime

now= datetime.now()
timestamp = datetime.timestamp(now)
print(timestamp)

d = "02/01/1970"
then = datetime.strptime(d, "%d/%m/%Y")
timestamp = datetime.timestamp(then)
print(timestamp)

def try_one():
    year = 365*86400*(-66)
    for i in range(0,367):
        timestamp = i*86400 - 43200 + year
        dt_object = datetime.fromtimestamp(timestamp)
        print(dt_object)
        
def try_two():
    year = 365*86400 
    leap_year = 366*86400 
    timestamp = 0 - 43200
    for i in range(0,100):
        dt_object = datetime.fromtimestamp(timestamp)
        print(dt_object)
        
        
        if (2+i)%4 == 0:
            timestamp += leap_year
            print("Add 366")
        else:
            timestamp += year
            print("Add 365")
        if str(dt_object.year) == "1974":
            timestamp -= 3600

def try_three():
    year = 365*86400 
    leap_year = 366*86400 
    timestamp = 0 - 43200
    for i in range(0,500):
        dt_object = datetime.fromtimestamp(timestamp)
        print(dt_object)
        
        
        if (2+i)%4 == 3 and (int(dt_object.year)-1)%100 != 0:
            timestamp -= leap_year
            #print("Subtract 366")
        else:
            timestamp -= year
            #print("Subtract 365")
        if str(dt_object.year) == "1929":
            timestamp += 1800
        elif str(dt_object.year) == "1869":
            timestamp -= 544
            #print("shift")
        elif str(dt_object.year) == "1600":
            timestamp -= 86400
            
        
        
        
            

#try_two()
try_three()
    
