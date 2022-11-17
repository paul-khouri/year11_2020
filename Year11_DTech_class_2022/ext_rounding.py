import math

my_num = 60
rounding_num = 7.8



def round_to(n, round_to):
    rounded = round(n/round_to)* round_to
    return rounded

print(round_to(88, 7))
