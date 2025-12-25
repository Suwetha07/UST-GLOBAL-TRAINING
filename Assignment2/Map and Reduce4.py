#Write a Python program that uses reduce() to find the greatest common divisor (GCD) of a list of numbers.
from functools import reduce
import math
numbers = [24,36,60,80]
gcd = reduce(math.gcd, numbers)
print(gcd)

