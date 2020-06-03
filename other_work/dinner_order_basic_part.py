#constants
MAIN_PRICE = 12.5
DESSERT_PRICE = 6.0
DRINKS_PRICE = 3.55

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

print(ext_gst)
print(my_gst)
print(my_to_pay)
