#constants
MAIN_PRICE = 12.5
DESSERT_PRICE = 6.0
DRINKS_PRICE = 3.55

super_grand_total = 0

continue_program = True
while continue_program == True:
    # input variables
    mains = int(input("How many mains would you like to order?: "))
    desserts = int(input("How many desserts would you like to order?: "))
    drinks = int(input("How many drinks would you like to order?: "))

    #calulate costs
    mains_total = mains * MAIN_PRICE
    desserts_total = desserts * DESSERT_PRICE
    drinks_total = drinks * DRINKS_PRICE

    ext_gst = mains_total + desserts_total + drinks_total
    my_gst = ext_gst*0.15
    my_to_pay = ext_gst + my_gst
    # adding on current bill to the overall total bills
    super_grand_total += my_to_pay

    print("-"*40)
    print("Bill's Diner")
    print("-"*40)
    print("{:<3}{:10}at ${:<10.2f}= ${:.2f}".format(mains,"mains", MAIN_PRICE, mains_total))
    print("{:<3}{:10}at ${:<10.2f}= ${:.2f}".format(desserts,"desserts", DESSERT_PRICE, desserts_total))
    print("{:<3}{:10}at ${:<10.2f}= ${:.2f}".format(drinks,"drinks", DRINKS_PRICE, drinks_total))
    print("-"*40)
    print("{:>27}= ${}".format("Total  ", ext_gst))
    print("{:>27}= ${:.2f}".format("GST  ", my_gst))
    print("{:>27}= ${:.2f}".format("To Pay  ", my_to_pay))
    print("-"*40)
    print("Thankyou")
    print("-"*40)

    user_input = input("Would you like to start a new order? (Y/N) -> ")
    if user_input == "Y":
        print("New order starting")
    elif user_input == "N":
        print("Thankyou")
        # set program condition to false
        continue_program = False
    else:
        continue_program = False
        print("You input was not a valid entry")

output = "The total amount charged tonight is {}".format(super_grand_total)
print(output)

print("The program has ended")
