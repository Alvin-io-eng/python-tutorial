def main():
    users = []
    name = str(input("Enter your Username: "))
    password = str(input("Enter your Password: "))
    confirm_password = str(input("Confirm your Password: "))
    details_validation(name, password, confirm_password)
    add_data(users, name, password)
    login(users)
    
    

def details_validation(name, password, confirm_password):
    if " " in name:
        print("There should be no spaces in your Username")
    if password != confirm_password:
        # print("Your Passwords do not match")
        return "Your Passwords do not match"

def add_data(users, name, password):
    data = {
        "name": name,
        "password":password
    }
    users.append(data)

    # print(users)

def login(users):
    name = str(input("Enter your name:  "))
    password = str(input("Enter your password: "))

    for data in users:
        if name:
            if password != data["password"]:
                print("You have entered the wrong password")
            else:
                print("You have logged in successfully")
        else:
            print(f"No {name} found in the database")








if __name__ == "__main__":
    main()