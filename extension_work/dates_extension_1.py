import re
from datetime import datetime, date

my_date = "20/04/1998"
today_date = datetime.today()


def check_date_format(d):
    x = re.findall("[0-9]+/[0-9]+/[0-9]+", d)
    print(x)
    return x[0]

d=check_date_format(my_date)

def create_date_object(d):
    date_object = datetime.strptime(d, "%d/%m/%Y")
    return date_object


date_object=create_date_object(d)
print(date_object)
print(date_object.strftime("%A"))
print(today_date)

date_delta = today_date - date_object
print(date_delta)
print(date_object.strftime("%j"))
print(today_date.year)
    
# print date as day of week etc
