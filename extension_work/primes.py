

def get_primes(max_num):
    prime_list=[2,3]
    for i in range(6,max_num,6):
        for n in [i-1, i+1]:
            found_prime = True
            for p in prime_list:
                if n%p == 0:
                    found_prime = False
                    # the number is not prime
                    break
            if found_prime:
                prime_list.append(n)
    return prime_list

my_primes= get_primes(200000)
#print(my_primes)
print("Got primes")
temp = ""
for i in range(0, len(my_primes), 1):
    temp += "{:10}".format(my_primes[i])
    if (i+1)%6 == 0 and i!=0:
        print(temp)
        temp=""
print(temp)
    

            
    
