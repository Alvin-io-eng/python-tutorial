# ADVANCED EXAMPLES
""" ADVANCED EXAMPLES """

from functools import reduce

"""
REDUCE function
It is going to reduce down some kind of iterable object to a single value by utilising a reduce function

"""

numbers = [1,2,3,4,5]

# Using reduce to sum  the list without initializer
sum_of_numbers = reduce(lambda acc, x: acc + x, numbers)
"""
the above function will accept 2 arguments; 
...acc - accumulated value,
...x - the next value that we are gonna be processing from our iterable object
.....by default the acc when we start will be the 1st value i the iterable set and x will be the next one
.....so when we start acc = 1 , x = 2 : 1 + 2 = 3 
.....then acc = 3 , x = 3 : 3 + 3 = 6 -> acc = 6 ...onwards till the last digit
.....What is reduce doing?
....>it is taking whatever was returned from the last call passing that as the next accumulator 
.....,and then adding in whatever that additional value is that we are processing

"""
print(sum_of_numbers) # Output = 15

# Using reduce to find the maximum value
max_values = reduce(lambda acc, x: acc if acc > x else x, numbers)
"""
we have written an inline if statement and thats the expression we are returning from lambda function which is valid
...acc if acc > x else x
.....we are going to return the accumulated (acc) value (if) the (acc) is greater(>) than (x) otherwise (else) I'll just return (x)
.....means we are going to keep the largest value we have
......but as soon some value is larger than that then we'll return that one
.......otherwise we'll keep the previous on because it was larger

"""
print(max_values)

# last bonus example
fancy_comp = {x: (lambda x:x*x) (x) for x in range(5)}
print(fancy_comp)