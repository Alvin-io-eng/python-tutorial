# MAP & FILTER, SORT
""" MAP & FILTER, SORT """

# Here is where lambda functions are most useful in MAP func & FILTER func & SORT

"""
MAP function
What a map function does is it takes some list/iterable object and apply a function to every sngles value inside of it
"""

my_numbers = (1,2,3,4,5,6,7,8,9,10)

def square(x):
    return x ** 2

# in this case we take all the numbers in my numbers and pass them to the square function 
# and generate a new list {list()} that contains all of those results/squares
squares = list(map(square, my_numbers))
f  = list(my_numbers)
print(squares)
# print(type(f))
# print(type(my_numbers))

# we could argue the square function is not needed to be used again since 
# lambda would be more elegant and the square function is redundantly defined
# instead we can do this 

squares = list(map(lambda a : a ** 2, my_numbers))

print(squares)

"""
FILTER function
The filter function it will apply a function to every single value of an inside of a list/iterable object
...and if the function returns true it will keep this obect and if false it will reject it
...filtering some kind of iterable object for us

"""

evens = list(filter(lambda a: a % 2 == 0,my_numbers))
print(evens)

"""
SORT function
lamda function can be used as the key function for some kind of sort
...in the below example, we have a list and few different tuples inside: we have a (number, letter and a string)
...it kind of ambigous which element we wanna sort by or how we should sort the arious elements
...we can specifiy how to sort that by passing a key function 
...in this case the key function will take any one of our objects and strip out the element at index 1
...which is going to be the letter
...this will be the element python will sort based on and is also a common use case for lambda
"""
values = [(1,"b","Hello"),(2,"a","World"),(3,"c","ok")]
sorted_values = sorted(values, key=lambda x : x[1] + x[2])
# sorted_values = list(sorted(values, key=lambda x : x [1]))
print(list(sorted_values))
# print(sorted_values)