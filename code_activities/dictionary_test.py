import time
start= time.time()
t= time.localtime()
print(t)
print(start)




word = "halloween"
char_list = list(word)
print(char_list)
char_list_chosen=["l", "w", "e"]
outstring = ""
for x in char_list:
    if x in char_list_chosen:
        outstring += " "+x+" "
    else:
        outstring += " _ "
print(outstring)
        





question_one = {
    "question": "What is the capital of France?",
    "A": "Paris",
    "B": "Moscow",
    "C": "Shanghai",
    "answer": "C"
    }

print(question_one["question"])
for x,y in question_one.items():
    if x != "question" and x != "answer":
        print("{}) {}".format(x,y))

for x,y in question_one.items():
    if len(x)== 1:
        print("{}) {}".format(x,y))
        
answer = input("Enter your choice ")
if answer == question_one["answer"]:
    print(" Brilliant ")
end=time.time()
print(end)
print(end-start)
count = 0
while count < 3:
    temp={}
    temp["english"]= input("Enter your english word")
    temp["thai"] = input("Enter your thai word")
    print(temp)
    count +=1
    





