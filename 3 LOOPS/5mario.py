# print("#")
# print("#")
# print("#")

# for _ in range(3):
#    print("#")
    
def main():
   print_column(3)
   print_row(3)
   print_triangle(3)
   print_square(3)

def print_column(height):
   for _ in range(height):
      print("#")

def print_triangle(base):
    for i in range(base):
      print("* " * (i + 1))

def print_row(width):
   print("? " * width)
#    for _ in range(width):
#       print("? ",end="")

""" My own implementation of printing a square which seems t be more suitable for a rectangle """
# def print_square(size):
#    size_col = size
#    size_row = size 
#    for i in range(size_col):
#       print("# " * size_row)

def print_square(size):
   # for each row in square
   for i in range(size):

    # for each brick in row
    for j in range(size):
       
       # print brick
       print("@ ", end="")

    print()         

# def print_square(size):
#    # for each row in square
#    for i in range(size):
#       print("$ " * size)

# def print_square(size):
#    # for each row in square
#    for i in range(size):
#       print_row(size)

      

main()
