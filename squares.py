__author__ = 'Ernest'
# http://goo.gl/6bmW5U
'''
Python comprehensions are syntactic constructs that enable sequences to be
built from other sequences in a clear and concise manner.
Python comprehensions are of three types namely:
list comprehensions,
set comprehensions and
dict comprehensions.
List comprehension constructs have been part of python since python 2.0
while set and dict comprehensions have been part of python since python 2.7.
'''

# this is the normal way of creating a list.
squares = []
for x in range(10):
    squares.append(x**2)

print squares

# this is the same list written, but using list comprehension.
squares2 = [x**2 for x in range(10)]
print squares2

# here is how to print just the even numbers

even_squares = [i**2 for i in range(10) if i % 2 == 0]
print even_squares
