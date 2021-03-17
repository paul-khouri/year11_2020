# Trial idea 1
import random
token_list = ["unicorn", "horse", "zebra", "donkey"]
chosen_token = random.choice(token_list)
print(chosen_token)

#loop test
# to make sure all the tokens are getting chosen ,
# roughly equally
count = 0
while count < 100:
    chosen_token = random.choice(token_list)
    print(chosen_token)
    count += 1
    

