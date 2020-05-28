import random
# get token
tokens = ["horse", "zebra" , "donkey", "unicorn"]
player_token = random.choice(tokens)
print(player_token)
# test random
for i in range(0,20):
    player_token = random.choice(tokens)
    print(player_token)
    
