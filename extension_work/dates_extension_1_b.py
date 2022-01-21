from datetime import datetime, timedelta

# todays date with time set to 0:0:0
today_date = datetime.today()
print(today_date)
print(today_date.year)
print(today_date.month)
print(today_date.day)
print(today_date.hour)
print(today_date.minute)
print(today_date.second)
# millions of second
print(today_date.microsecond)
today_date = today_date.replace(hour = 0, minute=0, second=0, microsecond = 0)
print(today_date)

other_today_date = datetime.today()
date_string = other_today_date.strftime("%d/%m/%Y")
print(date_string)
clean_today = datetime.strptime(date_string, "%d/%m/%Y")
print(clean_today)

my_birthday = "20/07/1967"
birthday_object = datetime.strptime(my_birthday, "%d/%m/%Y")
print(birthday_object)
print(birthday_object.year)
date_delta = clean_today - birthday_object
print(type(date_delta))
print(date_delta.total_seconds())
print(str(date_delta))
print(int(date_delta.days))

