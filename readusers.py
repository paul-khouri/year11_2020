


my_file=open("user_info.txt","r")
def print_out_file():
    print("Called")
    for txt in my_file:
        print(txt)
    

def sign_in():
    name = input("Please enter your username: ")
    user_name_found = False
    for txt in my_file:
        txt = txt.replace("\n", "")
        txt = txt.replace(" ", "")
        info = txt.split(",")
        if info[0] == name:
            password = input("Please enter your password: ")
            user_name_found = True
            if info[1] == password:
                print("successful")
                return name
            else:
                print("Invalid password")
    if not user_name_found:
        print("Your user name is not recognised")

def get_name():
    name = input("Please enter your player name")
    return name

def sign_up():
    user_name = input("Please enter a username: ")
    # check if exists
    user_name_okay = True
    for txt in my_file:
        txt = txt.replace("\n", "")
        txt = txt.replace(" ", "")
        info = txt.split(",")
        if info[0] == user_name:
            print("This user name is already taken")
            user_name_okay = False
            break
    if user_name_okay:
        password = input("Please enter a password: ")
        write_file = open("user_info.txt", "a")
        new_user = "{},{}\n".format(user_name, password)
        write_file.write(new_user)
        write_file.close()
        latest_file=open("user_info.txt","r")
        for txt in latest_file:
            print(txt)
        
        
def get_user():
    options={
        "A": "Play as Guest",
        "B": "Sign in",
        "C": "Sign up"
        }
    for x, y in options.items():
        print("{}: {}".format(x,y))
    choice = input("Please choose your option").upper()
    if choice == "A":
        get_name()
    elif choice == "B":
        sign_in()
    elif choice == "C":
        sign_up()
              
#sign_in()

get_user()






