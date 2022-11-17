import random

def get_factors(n):
  factor_count = 2
  c=2
  while c < n:
    if n%c == 0:
      factor_count += 1
      #print(c)
    c += 1
  return factor_count

def get_digit_sum(n):
    str_num = str(n)
    digit_sum = 0
    for d in str_num:
        digit_sum += int(d)
        #print(d)
    return digit_sum

def find_number(mn,mx,n, c=0):
    if c==10:
        print("Finding error")
        return None
    #test midpoint
    mid_p = round((mn+mx)/2)
    print(mid_p)
    if mid_p == n:
        print("Found")
        return None
    elif mid_p > n:
        c+=1
        mid_p -=1
        find_number(mn, mid_p, n, c)
    else:
        c+=1
        mid_p +=1
        find_number(mid_p, mx , n, c)

def test(mn,mx):
    c = mn
    while c <= mx:
        find_number(mn,mx,c)
        c+=1

        
    
    
        

# set min max boundaries
min_num = 1
max_num = 100
# generate number
secret_num = random.randint(min_num, max_num)
test(min_num, max_num)
find_number(min_num, max_num, secret_num)

output = "A secret number between {} and {} has been chosen.".format(min_num, max_num)
print(output)
output = "The number has {} factors including 1 and itself".format(get_factors(secret_num))
print(output)
output = "The sum of the digits is {}".format(get_digit_sum(secret_num))
print(output)
guess = int( input("Please enter your guess: ") )
# check user guess
if guess < secret_num:
    print("Your guess is too small")
elif guess > secret_num:
    print("Your guess is too large")
elif guess == secret_num:
    print("You guessed it!")
else:
    print("Error")
# testing
output = "The number was {}".format(secret_num)
print(output)
