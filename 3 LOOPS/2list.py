# FOR loop allows you to iterate over a list of items

for i in  [0,1,2]:
    print("meow0")

for i in range(3):
    print("meow1")

for _ in range(3):
    print("meow2")

print("meow3" * 3)
print("meow3\n" * 3)
print("meow3\n" * 3, end="")

# now lets take user's input that's matches a certain composite in our case a +ve integer

n = int(input("What's n? "))
if n < 0:
    n = int(input("What's n? "))
    if n < 0:
       n = int(input("What's n? "))
# instead of writing alot of if's

while True:
    n = int(input("What's n? "))
    if n < 0:
        continue
    else:
        break

# OR

while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow3")

"""
def main():
    meow(3)

def meow(n):
    for _ in range(n):
     print("meow4")

def main():
    number = get_number()
    print(type(number))
    meow(number)

def get_number():
    while True:
       n = int(input("What's n? "))
       if n > 0:
          break
    return n     

def meow(n):
    for _ in range(n):
     print("meow5")

main()`
     
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
       n = int(input("What's n? "))
       if n > 0:
          return n     

def meow(n):
    for _ in range(n):
     print("meow5")

main()

"""