
high = 10
low = 1
error_int = "You have not entered an integer, please try again"
error_amount = ("You have not entered an appropriate amount\n"
                "it must be between $1 and $10")
msg = "Please choose between $1 and $10: "
get_value = False
while get_value == False:
    try:
        player_amount = int(input(msg))
    except ValueError:
        print(error_int)
        continue
    if player_amount < low or player_amount > high:
        print(error_amount)
        continue
    get_value = True

