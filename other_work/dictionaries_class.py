# python dictionaries
# they have a key and a value (and can have many of them)
# simple example
car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
    }

#print(car["brand"])
#print(car["year"])

question_one = {
    "question": "What is the capital of France?   ",
    "answer" : "Paris"
    }


user_answer = input(question_one["question"])
if user_answer == question_one["answer"]:
    print("You are a star")
else:
    print("Unortunately this is not correct")

# multichoice

multi_q = {
    "question": "What is the capital of France? ",
    "A" : "Paris",
    "B" : "Moscow",
    "C" : "Shanghai",
    "answer" : "A"
    }

# we loop through dictionaries

for x, y in multi_q.items():
    print("{} , {}".format(x,y))


# running a quiz question
print(multi_q["question"])













    
    


