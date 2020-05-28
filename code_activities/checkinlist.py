guess_list = [45,78,90,21,7]

guess=int(input("Enter your guess"))


while guess in guess_list:
    guess = int(input("You have already tried this number,\
have another guess"))
guess_list.append(guess)
print(guess_list)
