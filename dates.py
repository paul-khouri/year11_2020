from datetime import datetime

def create_date_string():
    my_date = datetime.now()
    print(my_date)
    my_string = my_date.strftime("%H:%m %d/%m/%Y")
    print(my_string)


create_date_string()
    
