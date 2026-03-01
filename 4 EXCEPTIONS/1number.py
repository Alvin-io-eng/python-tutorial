# try:
#     x = int(input("What is x? "))
#     print(f"x is {x}")
# except ValueError:
# # except ValueError as x:
#     print("x is not an integer")
#     # print(f"x - {x} is not an integer")
#     # print(x)

# try:
#     x = int(input("What is x? "))
# except ValueError:
# # except ValueError as x:
#     print("x is not an integer")
#     # print(f"x - {x} is not an integer")
#     # print(x)

# print(f"x is {x}")

# try:
#     x = int(input("What is x? "))
# except ValueError:
# # except ValueError as x:
#     print("x is not an integer")
#     # print(f"x - {x} is not an integer")
#     # print(x)
# else:
#     print(f"x is {x}")

# if we want to continue endlessly without breaking untill we get our integer

# while True:
#     try:
#         x = int(input("What is x? "))
#     except ValueError:
#         print("x is not an integer")
#     else: 
#         break

# print(f"x is {x}")

# while True:
#      try:
#         x = int(input("What is x? "))
#         break
#      except ValueError:
#         print("x is not an integer")

# print(f"x is {x}")

def main():
    # x = get_int()
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
      try:
        #   x = int(input("What is x? "))
        #   return x
        #  return int(input("What is x? "))
         return int(input(prompt))
      except ValueError:
        # print("x is not an integer")
        pass
    #   else: 
    #     # break
    #     return x   

main()