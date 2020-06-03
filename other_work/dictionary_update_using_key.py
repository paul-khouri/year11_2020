

def run_main():
     bernie = 0
     joe = 0
     
     my_dictionary = {
          "A" : ["bernie" , 10],
          "B" : ["joe", 16]
     }
     
     print("bernie {} ; joe {} ".format(bernie, joe) )
     key = input("Q")
     
     if my_dictionary[key][0] == "bernie":
          bernie += my_dictionary[key][1]
     elif my_dictionary[key][0] == "joe":
          joe += my_dictionary[key][1]
     else:
          print("Unrecognised variable name")
          
     print( "bernie {} ; joe {} ".format(bernie, joe) )

run_main()


