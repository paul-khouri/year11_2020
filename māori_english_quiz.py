
M=["aroha", "awa", "haka", "hangi", "hapu", "hīkoi"]
E=["Love","River","A Māori dance.","Food from an earth oven","A sub-tribe","A walk"]
#print(len(M))
#print(len(E))



def macron_check(a):
    word= a
    macron = ["ī","ā", "ō", "ū"]
    char = ["i","a", "o", "u"]
    for c in word:
        if c in ["ī","ā", "ō", "ū"]:
            word = word.replace(c, char[macron.index(c)])
    return word

#print(macron_check("hīkoi"))
            
        

c = 0
while c < len(E):
    question = "What is the Māori word for '{}' ?".format(E[c])
    answer = input(question).lower().strip()
    correct_answer = macron_check( M[c].lower().strip() )
    if answer == correct_answer:
        print("Brilliant")
    else:
        print("unfortunately this is not correct")
        response = "the Māori word for '{}' is '{}'.".format(E[c], M[c])
        print(response)
    c += 1
print("Program has ended")
        

	
	
	
	
	
	
