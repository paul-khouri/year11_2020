# print todays date
# ask the user for their birthday
# extract as regex
# state the day of the week birthday
# state the number of the day of the year the birthday was on
# work out how many days until your birthday
from datetime import datetime
import re
from dateutil.relativedelta import relativedelta

def get_birthday():
    birthday = input("Please enter your birthday in the format dd/mm/yyyy:-> ")
    x = re.findall("[0-9]+/[0-9]+/[0-9]+", birthday)
    if len(x) == 0:
        print("Error entering valid date")
        return None
    else:
        output = "The birthday you have entered is: {}".format(x[0])
        print(output)
        return x[0]


def run_birthday(d):
    # create datetime object
    birthday_obj = datetime.strptime(d, "%d/%m/%Y")
    day_week = birthday_obj.strftime("%A")
    output = "You were born on a {}".format(day_week)
    print(output)
    day_number = birthday_obj.strftime("%j")
    output = "You were born on day {} of the year".format(day_number)
    print(output)
    

    # get today's date for comparison
    today_date = datetime.today()
    # clean up so hours etc all 0
    today_date = today_date.replace(hour = 0, minute=0, second=0, microsecond = 0)
    output = "Today's date is {}".format(datetime.strftime(today_date, "%d/%m/%Y"))
    # state age
    age = relativedelta(today_date, birthday_obj)
    output = "You are {} years, {} months and {} days old".format(age.years, age.months, age.days)
    print(output)
    
    # update birthday so year is the same as this
    birthday_obj = birthday_obj.replace(year = today_date.year)
 
    # check if updated birthday is ahead or behind today
    # if it is behind, addon one more year
    if birthday_obj < today_date:
        birthday_obj = birthday_obj.replace(year = today_date.year+1)
    time_to_birthday = birthday_obj - today_date
    output = "There are {} days to your birthday".format(time_to_birthday.days)
    print(output)
        


d=get_birthday()
if d:
    run_birthday(d)
else:
    print("Invalid birthday entered")
    
    
