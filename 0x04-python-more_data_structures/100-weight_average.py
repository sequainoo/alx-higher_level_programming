#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    quotient, divisor = 0, 0
    for score, weight in my_list:
        quotient += score * weight
        divisor += weight
    weighted_average = quotient / divisor
    return weighted_average
