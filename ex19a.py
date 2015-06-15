#!/usr/bin/env python
__author__ = 'Ernest'

# this is an exercise from the slideshare on lpthw.

a = "How many miles per gallon does your car get? "
b = "What is the current price of gas, per gallon? (Please use a decimal, like this 2.95 )"
c = "What is the length of your trip in miles? "


mpg = float(raw_input(a))
price_of_gas = float(raw_input(b))
distance = float(raw_input(c))

# using float will allow decimal numbers
# here are some new comments for this file


def journey_cost(mpg, price_of_gas, distance):
    total_fuel = distance / mpg
    cost = total_fuel * price_of_gas
    return cost

total = journey_cost(mpg, price_of_gas, distance)
print "The cost of this journey will be %d pounds." % total
