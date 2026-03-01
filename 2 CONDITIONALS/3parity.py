# Check if a number is EVEN or ODD
x = int(input("What's x ? "))

if x%2 == 0:
    print(f"The number x = {x} is even")
else:
    print(f"The number x = {x} is odd")

# OR

def main():
    x = int(input("What's x ? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")
    
def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False
    
"""

def is_even():
    return True if n % 2 == 0 else False

def is_even():
    return n % 2 == 0

"""
    
main()