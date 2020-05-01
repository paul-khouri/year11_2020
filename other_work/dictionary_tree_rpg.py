tree = {

    'node':{
        'left': 'node_left',
        'right': 'node_right',
        'content': 'I am node' 
        },
    'node_left':{
        'parent' : 'node',
        'left': 'node_left_left',
        'right': 'node_left_right',
        'content': 'I am node_left'
        },
    'node_right':{
        'parent' : 'node',
        'left': 'node_right_left',
        'right': 'node_right_right',
        'content': 'I am node_right'
        },
    'node_left_left':{
        'parent' : 'node_left',
        'content': 'I am node_left_left'
    },
    'node_left_right':{
        'parent' : 'node_left',
        'content': 'I am node_left_right'
        },
    'node_right_left':{
        'parent' : 'node_right',
        'content': 'I am node_right_left'
        },
    'node_right_right':{
        'parent' : 'node_right',
        'content': 'I am node_right_right'
        }
    
    }

chosen_item = tree['node']
run_loop = True
while run_loop:
    print(chosen_item['content'])
    user_choice=input("Choose 'left' or 'right' or 'parent' -> ")
    if user_choice == "q":
        run_loop = False
    elif user_choice in chosen_item:
        chosen_item =tree[chosen_item[user_choice]]
    elif user_choice in ['parent', 'left', 'right']:
        print("You can't go that way")
    else:
        print("Invalid entry")
    





