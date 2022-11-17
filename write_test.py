def create_write_file():
    confirm = input("Eeeeek! This will delete and create a fresh file, all data will be deleted. Y or N!")
    if confirm == "Y":
        write_file=open("results.csv", mode="w")
        header = "Date, Name, Score, Questions\n"
        write_file.write(header)
        write_file.close()
        print("Fresh file created")

def add_result():
    result="20/07/89, Paul, 3, 5\n"
    write_file = open("results.csv", mode="a")
    write_file.write(result)
    write_file.close()

def read_file():
    write_file = open("results.csv", mode="r")
    for x in write_file:
        print(x, end="")

create_write_file()
add_result()
add_result()
read_file()
    






