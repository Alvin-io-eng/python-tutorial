# now lets say I want to read content in the file
# "r" - for reading
with open("names.txt","r") as file:
    lines = file.readlines()
    # it will bring a list of items

# print(lines)
for line in lines:
    # print("Hello ", line) # will have double new lines
    # print("Hello ", line, end="") # ok but not neccesarily better 
    print("Hello ", line.rstrip()) # now this will strip off the end of a line so that print to handle printing of everything

# more elegant
with open("names.txt","r") as file:
    for line in file:
        print("Hello ", line.rstrip())

# lets say we want to sort it
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"Hello, {name}")

# OR

"""

with open("names.txt") as file:
    for line in sorted(file):
        names.append(line.rstrip())

"""