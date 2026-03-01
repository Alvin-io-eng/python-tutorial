correct_password = "Python123"
user_input = ""

i = 0

while i != 3:
    user_input = input("Password: ")
    if user_input == correct_password:
        print("Successful login")
    else: 
        i += 1
        print("wrong password attempts")