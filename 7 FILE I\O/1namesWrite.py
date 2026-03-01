# names = []

# for _ in range(3):
#     # print(f"Hello, {name}")
#     names.append(input("What's your name? "))

# for name in sorted(names):
#     print(f"Hello, {name}")

# After using the above program the names will be lost so lets start implementing file I/O

name = input("What's your name? ")

"""
# lets save the value to a file

file = open("names.txt","w")
"w" - creates the file and when never we type in a new name it is over written
file.write(name)
file.close()

"""
# 

"""
file = open("names.txt","a")
# "a" - creates the file but this time it appends the new name  
file.write(name)
file.write(f"{name}\n")
file.close()

"""
# 

"""
the file this time if I type these names;Hermione, Harry, Ron; the output will be ; HermioneHarryRon

but it is not concatinating them per say so we can write this way 
file.write(f"{name}\n")

"""
# specifies in this context I want you to open and automatically close this file
with open("names.txt","a") as file:
    file.write(f"{name}")

