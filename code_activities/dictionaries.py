car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")

print(x)

quiz_one = {
    "question" : "What is the capital of France? ",
    "answer"   : "Paris"
    }
quiz_two = {
    "question" : "What is the capital of Spain? ",
    "answer"   : "Madrid"
    }
quiz_three = {
    "question" : "What is the capital of Germany? ",
    "answer"   : "Berlin"
    }
print(quiz_one.get("question"))

user_answer = input( quiz_one.get("question") )
if user_answer == quiz_one.get("answer"):
    print("Correct")
user_answer = input( quiz_two.get("question") )
if user_answer == quiz_two.get("answer"):
    print("Correct")
user_answer = input( quiz_three.get("question") )
if user_answer == quiz_three.get("answer"):
    print("Correct")

quiz_set = [
    {
    "question" : "What is the capital of France? ",
    "answer"   : "Paris"
    },
    {
    "question" : "What is the capital of Spain? ",
    "answer"   : "Madrid"
    },
    {
    "question" : "What is the capital of Germany? ",
    "answer"   : "Berlin"
    }
    ]

for x in quiz_set:
    user_answer = input( x.get("question") )
    if user_answer == x.get("answer"):
        print("Correct")
