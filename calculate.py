# import math functions from math_lib.py

import math_lib as ml

# calculate the average of 2 numbers


def average(a, b):
    sum = ml.add(a, b)
    print(ml.div(sum, 2))


average(a, b)
