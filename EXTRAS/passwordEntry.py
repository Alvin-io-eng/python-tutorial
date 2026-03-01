correct_password = "Python123"
user_input = ""
i = 3

while i != 0:
    user_input = input("Enter your Password: ")
    if user_input != correct_password:
        i -= 1
        print(f"Wrong Password {i} attempts left")
    else:
        print("Correct password")
        break

 