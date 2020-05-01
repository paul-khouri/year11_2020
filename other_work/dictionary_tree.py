zero = { "left": None, "right":None,
         "content": "level 2 - 0" }
two = { "left": None, "right": None,
        "content": "level 2 - 1" }
one_zero = { "left": zero, "right": two,
        "content": "level 1 - 0" }
two_zero = { "left": zero, "right": two,
        "content": "level 1 - 0" }


chosen_item = one
loop_run = True
while loop_run == True:
    print(chosen_item["content"])
    my_input = input("Choose L or R:  ")
    if my_input == "L":
        chosen_item = chosen_item["left"]
    else:
        chosen_item = chosen_item["right"]
    if chosen_item["left"] is None and chosen_item["right"] is None:
        print("At the bottom")
        loop_run = False
print("End of program")
        
    




