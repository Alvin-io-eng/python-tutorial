# lets say I want to print meow 3 times but the below way is not much efficient
print("meow0")
print("meow0")
print("meow0")

# that's why we have *while loop*

i = 3 

while  i != 0:
    print("meow1")
    i -= 1
    # OR
    # i = i - 1

i = 1

while  i <= 3:
    print("meow2")
    i += 1
    # OR
    # i = i + 1

i = 0

while  i < 3:
    print("meow3")
    i += 1
    # OR
    # i = i + 1