import random

nums = False


my_random_num= random.random()
print(my_random_num)

for i in range(0,10):
    if nums== True:
        my_random_num= random.randint(1000,6000)
        print(my_random_num)
    else:
        people_list=["olivia", "ruby", "tiffany", "joanne", "mary"]
        chosen_name = random.choice(people_list)
        print(chosen_name)


    
