#Trial idea 2
import random
token_list = ["unicorn", "horse", "zebra", "donkey"]
random_index = random.randint(0,3)
chosen_token = token_list[random_index]
print(chosen_token)

#loop test
# to make sure all the tokens are getting chosen ,
# roughly equally
count = 0
while count < 100:
    random_index = random.randint(0,3)
    chosen_token = token_list[random_index]
    print(chosen_token)
    count += 1
