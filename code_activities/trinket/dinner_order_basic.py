#constants
MAIN_PRICE = 12.5
DESSERT_PRICE = 6.0
DRINKS_PRICE = 3.55

#totalling variables (initially declared as 0)
mains_total = 0.0
desserts_total = 0.0
drinks_total = 0.0
ext_gst = 0.0

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
