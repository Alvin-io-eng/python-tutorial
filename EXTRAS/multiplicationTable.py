numbers = [1,2,3,4,5,6,7,8,9,10]

for number in numbers:
    multiple = 1
    while multiple <= 10:
       result = number * multiple
       if multiple == 1:
            print(f"{number} x {multiple} = {result}\n", end="")
       elif multiple == 2: 
           print(f"{number} x {multiple} = {result}\n", end="")
       elif multiple == 3: 
           print(f"{number} x {multiple} = {result}\n", end="")
       elif multiple == 4: 
           print(f"{number} x {multiple} = {result}\n", end="")
       elif multiple == 5: 
           print(f"{number} x {multiple} = {result}\n", end="")
       elif multiple == 6: 
           print(f"{number} x {multiple} = {result}\n", end="")
       elif multiple == 7: 
           print(f"{number} x {multiple} = {result}\n", end="")
       elif multiple == 8: 
           print(f"{number} x {multiple} = {result}\n", end="")
       elif multiple == 9: 
           print(f"{number} x {multiple} = {result}\n", end="")
       else:
           print(f"{number} x {multiple} = {result}\n", end="")           
       multiple += 1