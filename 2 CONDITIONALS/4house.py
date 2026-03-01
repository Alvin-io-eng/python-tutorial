# using MATCH
name = input("What's your name? ")

if name == "Harry":
    print("Griffindor")
elif name == "Hermione":
    print("Griffindor")
elif name == "Ron":
    print("Griffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")

# OR

name = input("What's your name? ")

if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Griffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")

# OR - match

name = input("What's your name? ")

match name:
    case "Harry":
        print("Grifindor")
    case "Hermione":
        print("Grifindor")
    case "Ron":
        print("Grifindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")

# OR
name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Griffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")


