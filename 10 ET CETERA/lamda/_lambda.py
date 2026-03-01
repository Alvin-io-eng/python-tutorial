# LAMBDA
""" LAMBDA """
"""
LAMBDA - Anonymous functions; functions without names - one line anonymous function
.........functions are objects too
.........in lamda we can pass any number of arguments but should be of one expression (any valid python expression) only eg.
.........a + b, a * a

"""
def square(a):
    return a*a

result = square(4)

print(result)

# ITS LAMBDA SUBTITUTE

f = lambda a : a * a

result = f(4)

print(result)

def addition(a,b):
    return a + b

result = addition(5,6)

print(result)

# ITS LAMBDA SUBSTITUTE

f = lambda a,b : a + b

resul = f(5,6)

print(resul)
