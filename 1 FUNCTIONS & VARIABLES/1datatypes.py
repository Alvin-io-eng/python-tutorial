# STRING
"""  STRING  """
# Ask user for their name
name =  input("Whats you name? ")

# PRINT function parameters & arguments - parameters="arguments"
"""
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

"""

# say hello to user
print("hello, ", end="???")
print(name)

print("hello,",name,sep="?????")

print('Hello "freind"')
print("Hello \"freind\"")

# format string (f-string)

print(f"Hello {name}")

# remove white space from str
name = name.strip()

# capitalise the first letter of only the first word eg. from alvin immanuel to Alvin immanuel
name = name.capitalize()
# capitalise the first letter of all the words eg. from alvin immanuel to Alvin Immanuel
name = name.title()

# remove white space from string and capitalise user's name
name = name.strip().title()
# OR
name =  input("Whats you name? ").strip().title()

print(name)
# Other string methods
"""
name =  input("Whats you name? ").strip().title()
# split user's name into first name and last name 

first, last = name.split(" ")

print(f"Hello {first}")

"""


# INTEGERS
"""  INT  """
# operators
"""
+ PLUS-operator
- MINUS-operator
* MULTIPLICATION-operator
** SQUARE
/ DIVISION-operator
// returns the division without remainder
% MODULUS-operator (returns the remainder)

"""
# These will concatinate strings
x = input("What's x ? ")
y = input("What's y ? ")

# To prevent the above bug
# nesting functions int(input())
x = int(input("What's x ? "))
y = int(input("What's y ? "))

# OR 
# z = int(x) + int(y)

z = x + y

print(z)
# OR
# x = int(input("What's x ? "))
# y = int(input("What's y ? "))
# print(x + y)
# print(int(input("What's x ? ")) + int(input("What's y ? ")))



# FLOAT
"""  FLOAT  """
# decimal point numbers

x = float(input("What's x ? "))
y = float(input("What's y ? "))
print(x + y)

# round a float point to integer
# ROUND function parameters & arguments parameters="arguments"
"""
round(number[, ndigits])

 only one number
 for square brackets[] means optional
 [, ndigits] - specify number of digits that you want the round function to round to 

"""
z = round(x + y)
print(z)
# the below func will print 1,000 if x = 999, y = 1
print(f"{z:,}")

z = x / y
z = round(z,2)
"""
z = round(x + y,2)
print(f"{z:.2f}")

"""
print(z)

# LIST
"""  LIST  """
# a way of containing multiple values all in the same place all in the same variables

list_eg = [0,1,2]

# TUPLE
""" TUPLE """
# is like an immutable list once data is defined in them 

tuple_eg = (1,2,3)

# DICTIONARY
"""  DICTIONARY  """
# a way of asssociating 'keys' : with 'value'
# eg.

student = {
    "Name" : "Alvin Immanuel",
    "Age" :  20,
    "Height(m)" : 171
    }

# on the right(Key) : on the left(Value)


