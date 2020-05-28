# get number of punnets boxes buckets
my_punnets = float(input("How many punnets have you filled? "))
my_boxes = float(input("How many boxes have you filled? "))
my_buckets = float(input("How many buckets have you filled? "))

#testing
#my_punnets = 2.5
#my_boxes = 1.75
#my_buckets = 3.5

punnet_weight = my_punnets*0.25
box_weight = my_boxes*1.5
bucket_weight = my_buckets*7

total_weight = punnet_weight + box_weight + bucket_weight

total_price = total_weight * 5
print("."*30)
print("{:20}{:>6.2f} kg".format("Punnet weight" , punnet_weight))
print("{:20}{:>6.2f} kg".format("Box weight" , box_weight))
print("{:20}{:>6.2f} kg".format("Bucket weight", bucket_weight))
print("."*30)
print("{:20}{:>6.2f} kg".format("Total weight", total_weight))
print("."*30)
print("."*30)
print("{:20} ${:>6.2f}".format("Price to charge", total_price))
print("."*30)
