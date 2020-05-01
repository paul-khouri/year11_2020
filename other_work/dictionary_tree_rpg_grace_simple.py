tree = {
# top level
    'node':{
        'yes': 'node_yes',
        'no': 'node_no',
        'content': 'Do you go to the park? '
        },
# level 1
    'node_yes':{
        'parent' : 'node',
        'yes': 'node_yes_yes',
        'no': 'node_yes_no',
        'content': 'You are at the park, do you go to the swings? ',
        'story' : 'She was at the Park.'
        
        },
    'node_no':{
        'parent' : 'node',
        'no': 'node_no_no',
        'yes': 'node_no_yes',
        'content': 'Do you go swimming? '
        },
# level 2
    'node_yes_yes':{
        'parent' : 'node_yes',
        'yes': 'node_yes_yes_yes',
        'no': 'node_yes_yes_no',
        'content': 'There is someone there, do you say hello? ',
        'story': 'She was at the swings'
    },
    'node_yes_no':{
        'parent' : 'node_yes',
        'yes':'node_yes_no_yes' ,
        'no' : 'node_yes_no_no',
        'content': 'Do you go to the slide? '
        },
    'node_no_yes':{
        'parent' : 'node_no',
        'yes':'node_no_yes_yes' ,
        'no' : 'node_no_yes_no',
        'content': 'At the pool, there is slide with people, do you go on it?'
        },
    'node_no_no':{
        'parent' : 'node_no',
        'yes': 'node_no_no_yes',
        'no': 'node_no_no_no',
        'content': 'Do you ride a bike'
        },
# level 3
    'node_yes_yes_yes':{
        'parent' : 'node_yes_yes',
        'yes':None ,
        'no' : None,
        'content': 'You make a new friend'
        },
    'node_yes_yes_no':{
        'parent' : 'node_yes_yes',
        'yes':None ,
        'no' : None,
        'content': 'You sit on the swing by yourself'
        },
    'node_yes_no_yes':{
        'parent' : 'node_yes_no',
        'yes':None ,
        'no' : None,
        'content': 'You enjoy playing on the slide'
        },
    'node_yes_no_no':{
        'parent' : 'node_yes_no',
        'yes':None ,
        'no' : None,
        'content': 'You head home because you don\'t like the park'
        },
    'node_no_yes_yes':{
        'parent' : 'node_no_yes',
        'yes':None ,
        'no' : None,
        'content': 'You enjoy the slide'
        },
    'node_no_yes_no':{
        'parent' : 'node_no_yes',
        'yes':None ,
        'no' : None,
        'content': 'You play in the pool and meet people'
        },
    'node_no_no_yes':{
        'parent' : 'node_no_no',
        'yes':None ,
        'no' : None,
        'content': 'You enjoy riding through your neighbourhood'
        },
    'node_no_no_no':{
        'parent' : 'node_no_no',
        'yes':None ,
        'no' : None,
        'content': 'You are impossible to find an activity for'
        }
    
    }
print(len(tree))
chosen_item = tree['node']
run_loop = True
while run_loop:
    print(chosen_item['content'])
    user_choice=input("Choose 'yes' or 'no' or 'back' -> ")
    if user_choice == 'back':
        user_choice = 'parent'
    if user_choice == "q":
        run_loop = False
    # this just double checks
    elif user_choice in chosen_item:
        if chosen_item[user_choice] in tree:
            chosen_item =tree[chosen_item[user_choice]]
        else:
            print("This option does not exist")
    else:
        print("Invalid entry")
    if chosen_item["yes"] is None and chosen_item["no"] is None:
        print(chosen_item['content'])
        print("The end")
        run_loop = False
        

    





