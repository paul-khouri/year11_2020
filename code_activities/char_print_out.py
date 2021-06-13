import random
print(chr(178))
print(chr(179))
print(chr(8308))
start = 97
shift = 0
letters = []
for i in range(0,26):
    print("{} & ".format(i), end="")
print()
for i in range(0,26):
    char_num = 97 +( i+shift)%26
    print("{} & ".format(chr(char_num)), end="")
    letters.append(chr(char_num))
print()

mixed = letters.copy()
random.shuffle(mixed)
print(letters)
print(mixed)
for x in letters:
    print("{} & ".format(x),  end="")
print()
for y in mixed:
    print("{} & ".format(y), end="")
    

#403,291,461,126,605,635,584,000,000
