# compare values and make decisions on those values
x = int(input("What's x? "))
y = int(input("What's y? "))

# (boolean expression - Yes/No OR True OR False answers) IF
if x < y:
    print("x is less than y")

if x > y:
    print("x is greater than y")

if x == y:
    print("x is equal to y")

# make it more concise make it more faster and better code longer term ELIF
if x < y:
    print("x is less than y")

elif x > y:
    print("x is greater than y")

elif x == y:
    print("x is equal to y")

# instead of asking a final question ELSE
if x < y:
    print("x is less than y")

elif x > y:
    print("x is greater than y")

else:
    print("x is equal to y")

# SIMPLIFYING AS ABOVE MAKES THE PROGRAM RUN FASTER

if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# OR
if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# OR
if x == y:
    print("x is equal to y")   
else:
    print("x is not equal to y")
