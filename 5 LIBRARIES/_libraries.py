# LIBRARIES
""" LIBRARIES """
# are files of code that (other people OR you) have written that you can use in your own program

# keywords
"""
IMPORT - allows you to import the function/content of a module
FROM
SLICES - a subset of a data structure eg.list

"""

# MODULE - library that has 1 OR more functions built into it
# PACKAGE - is python module/ multiple module that are organised inside of a folder

# libraries example
"""
RANDOM 
random.choice(seq) - random sequence of values eg. from a list ["Heads","Tails"]
random.randint(a,b) - random integer from the range of a to b including a and b 
random.shuffle(x) - takes a list of values and shuffles them up eg. x = ['jack','queen','king']

STATISTICS
statistics.mean()

COMMMAND-LINE ARGUMENTS
sys.argv - a variable argv(argument vector) list of all the words human typed in at there prompt before hitting enter
sys.exit() - exit the program

"""

# PACKAGES - a module implemented in a folder
"""
PYPI - python package index

eg
COWSAY - a cow to say sth

keyword 
PIP - a python program that enables you to install packages in you computer ie. pip install cowsay


"""

# APIs - Application Programming Interface
# 3rd party services that we can write code to talk to 
# many apis live on the internet
# so so long you have a browser or experience with python programming/any other language, you can write code that pretends to be a browser connected to that 3rd party api on a server and download some data that you can in cooperate to your program
# How? using the below package
"""
REQUESTS - Allows you to make WEB/INTERNET requests using python code essentially as if you were a browser your self (http/https)
JSON > (Javascript Object Notation) - is as a language augnostic(you can use any language) format for exchanging data between computers

"""

# creating you own packages
# you can create a file with a repeatable function so that you do not have to repeat yourself/ copy every now and again

"""
eg.
def main():
    hello(name = "World")
    goodbye(name = "World")

def hello(name):
    print(f"Hello, {name}")

def goodbye(name):
    print(f"Goodbye, {name}")

main()

if you import the above code and use it, it will always run the main function everytime before running the code you have on you new program where you've imported it. Instead do this; 

def main():
    hello(name = "World")
    goodbye(name = "World")

def hello(name):
    print(f"Hello, {name}")

def goodbye(name):
    print(f"Goodbye, {name}")

if __name__ == "__main__":
    main()

"""
# now what have we done
"""
__name__ > special symbol(variable) in python whose values is automatically set by python to be "__main__" when you run a file from the command line.

"""