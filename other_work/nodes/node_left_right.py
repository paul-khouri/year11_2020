import node_set


chosen_item = node_set.get_set()
loop_run = True
while loop_run == True:
    print(chosen_item["content"])
    if chosen_item["left"] is not None and chosen_item["right"] is not None:
        my_input = input("Choose L or R or U to go up:  ")
        if my_input == "L":
            chosen_item = chosen_item["left"]
        elif my_input == "R":
            chosen_item = chosen_item["right"]
        elif my_input == "U":
            if chosen_item["parent"] is not None:
                chosen_item = chosen_item["parent"]
            else:
                print("There is no up to go")
    else:
        print("You are at the bottom")
        my_input = input("U to go up or any other key to finish:  ")
        if my_input == "U":
            chosen_item = chosen_item["parent"]
        else:
            loop_run = False
print("End of program")
