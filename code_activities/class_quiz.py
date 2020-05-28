class Question:

    def __init__(self, question,answer, score):
        
        self.question = question
        self.answer = answer
        self.score = score
        
        self.user_answer = ""
        self.user_score = 0
        self.response_to_user = ""

    def make_question(self):
        msg = self.question
        self.user_answer = input(msg)
        if self.user_answer == self.answer:
            self.response_to_user = "Correct"
            self.user_score = self.score
        else:
            self.response_to_user = "Incorrect"

    def feedback(self):
        strOne = "For the question: "+self.question+ "\n"
        strTwo = "You answered: "+self.user_answer +"\n"
        strThree = "Your answer was "+self.response_to_user
        print(strOne + strTwo + strThree)

#q_one = Question("What is the capital of France?", "Paris", 10)
#q_one.make_question()
#q_one.feedback()
q_list = []
q_list.append(Question("What is the capital of France?", "Paris", 10))
q_list.append(Question("What is the capital of Belgium?", "Brussels", 10))
q_list.append(Question("What is the capital of Holland?", "Amstredam", 10))

count = 0
while count < len(q_list):
    q_list[count].make_question()
    count += 1

count = 0
while count < len(q_list):
    q_list[count].feedback()
    count += 1

        
            
            
        
        
