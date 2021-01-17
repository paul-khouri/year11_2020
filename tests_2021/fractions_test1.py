import sys
print(sys.path)
from fractions import Fraction as frac
print(frac(2,3)+frac(2,3))
entry_ = input("enter fraction -> ")
print(frac(entry_)+frac(2,3))
print(frac(5, 4).numerator)


