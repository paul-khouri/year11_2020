#Trial idea 4
import random
chosen_token = ""
random_num = random.randint(0,3)
if random_num == 0:
    chosen_token = "Unicorn"
elif random_num == 1:
    chosen_token = "Horse"
elif random_num == 2:
    chosen_token = "Zebra"
else:
    chosen_token = "Donkey"

print(chosen_token)
    
 
