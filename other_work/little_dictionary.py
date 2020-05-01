my_tree = {
     'node': {
          'yes':'node_yes',
          'no': 'node_no',
          'content': "Top of tree where would you like to go (yes/no)"
          },
     
     'node_yes':{
          'yes':None,
          'no': None,
          'content': "One YES down can go no further"},
     
     'node_no':{
          'yes':None,
          'no': None,
          'content': "One NO down can go no further"}

          }

run_loop = True
chosen_item= my_tree['node']
while run_loop == True:
     print(chosen_item['content'])
     if chosen_item['yes'] == None and chosen_item['no']== None:
          print("end")
          run_loop= False
     else:
          user_input = input("Choose yes or no")
          if user_input == "yes":
               key_name=chosen_item['yes']
               print(key_name)
               chosen_item = my_tree[key_name]
          elif user_input == "no":
               key_name=chosen_item['no']
               print(key_name)
               chosen_item = my_tree[key_name]
          else:
               print("Entry error")
