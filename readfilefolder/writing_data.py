from datetime import datetime
def create_results_file():
    confirm = input("Eeeeek! This will delete and create a fresh file, all data will be deleted. Y or N!")
    if confirm == "Y":
        write_file=open("results.csv", mode="w")
        header = "Date, Name, Score, Questions\n"
        write_file.write(header)
        write_file.close()
        print("Fresh file created")
        


def add_result(r):
    result = r
    write_file = open("results.csv", mode="a")
    write_file.write(result)
    write_file.close()

def print_results():
    write_file = open("results.csv", mode="r")
    for x in write_file:
        print(x, end="")
    print()



def create_date_string():
    my_date = datetime.now()
    my_string = my_date.strftime("%H:%M %d/%m/%Y")
    return my_string



result = "{},{},{},{}\n".format(create_date_string(), "julie", 9,10)

create_results_file()
add_result(result)
add_result(result)
add_result(result)
add_result(result)
print_results()

