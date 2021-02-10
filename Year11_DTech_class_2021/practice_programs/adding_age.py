# the input is "cast" into an integer (it is naturally a string)
age = int(  input("How old are you? -> ")   )
age_to_add = 20
new_age = age + age_to_add
output = "In {} years you will be {} years old".format(age_to_add, new_age)
print(output)
