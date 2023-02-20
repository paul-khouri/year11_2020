import random
num_list = [1,2,3,4,5,6,7,8,9,10,11,12,13]
random.shuffle(num_list)
#print(num_list)

score = 0
c=0
while c<12:
    first_number = num_list[c]
    second_number=num_list[c+1]
    output = "The number is {}".format(first_number)
    print(output)
    choice = input("Do you think the next number will be higher of lower (h/l) ?")
    output = "The next number is {}".format(second_number)
    print(output)
    if choice == "h" and second_number > first_number:
        print("yup its higher")
        score +=1 
    elif choice == "l" and second_number < first_number:
        print("yup its lower")
        score += 1
    else:
        score -= 3
        print("sorry it was the other way around")
    print()
    print("-"*30)
    print()
    c+=1
print(score)

    
