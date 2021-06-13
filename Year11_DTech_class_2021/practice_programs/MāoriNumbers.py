import math
number_list=["kore", "tahi", "rua" , "toru", "whā", "rima", "ono",
                         "whitu","waru","iwa", "tekau"]
#E waru, tangohia te toru, ka rima   Eight minus three is five
#tangohia minus (verb)
#E whitu, tāpirihia te whā, ka tekau mā tahi (7 + 4 = 11) (TRP 2010:261).
#Seven, plus four, equals eleven (7 + 4 = 11)
def numbers_to_hundred(n):
    output = ""
    if n <= 10:
        output = number_list[n]
        print(output)
    elif n%10 == 0:
        lead_digit = math.floor(n/10)
        output = "{} {}".format(number_list[lead_digit], number_list[10])
        print(output)
    elif n < 20:
        output = "tekau mā {}".format(number_list[n%10])
        print(output)
    elif n<100:
        output = "{} tekau mā {}".format( number_list[math.floor(n/10)], number_list[n%10])
        print(output)
    return output
        
        
    

def adding(X,Y):
    global score
    A = X
    B = Y
    C = X + Y
    output = "{} + {} = ".format(number_list[A],number_list[B])
    answer = int(input(output))
    if answer == C:
        print("answer is correct")
    else:
        print("Sorry, the answer was {}".format(C))

#adding(3,6)
c= 0
while c < 100:
    numbers_to_hundred(c)
    c += 1
