#Trial idea 3
import random
chosen_token = ""
random_num = random.random()
if random_num < 0.25:
    chosen_token = "Unicorn"
elif random_num < 0.5:
    chosen_token = "Horse"
elif random_num < 0.75:
    chosen_token = "Zebra"
else:
    chosen_token = "Donkey"

print(chosen_token)
    
 
