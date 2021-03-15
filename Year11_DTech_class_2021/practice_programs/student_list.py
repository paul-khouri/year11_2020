student_list = []
age_list = []

counter = 0
while counter < 5:
    name = input("Please enter student name: -> ")
    age=input("Please enter student age: -> ")
    student_list.append(name)
    age_list.append(age)
    counter += 1

print("All names and ages have been entered")

for i in range(0, len(student_list)):
    output = "{} : {} , {} years old".format(i, student_list[i], age_list[i])
    print(output)
