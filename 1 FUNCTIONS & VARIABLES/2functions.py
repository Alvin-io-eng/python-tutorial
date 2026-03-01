# DEF
"""  DEF  """
# def -  for define
# build a function that says hello
"""
name = input("What's your Name? ")

def hello():
    # greetings = "Hello, " + name    
    return print(f"Hello, {name}")

# print(hello())

greet = hello()
print(greet)

OUTPUT

alvin@alvin-HP-ProBook-430-G3:~/Desktop/Python$ python3 -u "/home/alvin/Desktop/Python/2functions.py"
What's your Name? Alvin
Hello, Alvin
None
alvin@alvin-HP-ProBook-430-G3:~/Desktop/Python$ 

"""
def hello(to="world"):
    print("Hello,",to)

# the world is added as a default value if there are no arguments
hello()

name = input("What's your Name? ")
# print(name)
hello(to = name)
# OR
# hello(name)

# NB:/ when using/callling a function you should define it to prevent NameError

def main():
    name = input("What's your name")
    hello2(name)

def hello2(to="world"):
    print("hello,",to)

main()

def main():
    x = int(input("What's x? "))
    print("x squared is ,",square(x))

def square(n):
    # or
    # return n ** 2
    # return pow(n, 2)
    return n * n

main()