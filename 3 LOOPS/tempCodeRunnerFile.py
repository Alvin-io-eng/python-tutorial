def print_square(size):
   size_col = size
   size_row = size 
   for i in range(size_col):
      print("# " * size_row)

def print_square(size):
   # for each row in square
   for i in range(size):

    # for each brick in row
    for j in range(size):
       
       # print brick
       print("@ ", end="")

    print()   