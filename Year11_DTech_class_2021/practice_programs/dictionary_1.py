question_one = {
    "M" : "maugna",
    "E" : "mountain"
    }
print(question_one)
answer = input(  "What does the Māori word  '{}' mean?: ".format(question_one["M"])   )
if answer == question_one["E"]:
    print("correct")
    question_one["result"] = 1
else:
    print("incorrect")
    question_one["result"] = 0

print(question_one)


