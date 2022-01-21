import re
from datetime import datetime

today_date = datetime.today()
print(today_date)
print(today_date.year)
print(today_date.day)


my_birthday = "20/07/1967"
birthday_object = datetime.strptime(my_birthday, "%d/%m/%Y")
print(birthday_object)
day_number = birthday_object.strftime("%j")
output = "I was born on day {} of the year".format(day_number)
print(output)
day_week = birthday_object.strftime("%A")
output = "I was born on a {}".format(day_week)
print(output)

birthday_object=birthday_object.replace(year=today_date.year)
print(birthday_object)
time_to_birthday = birthday_object-today_date
print(time_to_birthday)
