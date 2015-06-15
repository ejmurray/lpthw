#!/bin/python3
__author__ = 'Ernest'
# Functions and Variables


# this is the function that prints out the four lines below the section headings.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes od crackers" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


# this line prints the line below and then calls the function with the values 20 and 30
# these are put in the function and then run.
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# this line uses two variables to use as the two arguments for the function
# it then calls the function cheese_and_crackers
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# this line does maths inside the function. In this case addition
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# this line combines variables and does an addition
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# here is the function that I've added
print "Here is the line that I'm adding to make up the rest of the exercise"
cheese_and_crackers(amount_of_cheese - 8, amount_of_crackers - 40)
