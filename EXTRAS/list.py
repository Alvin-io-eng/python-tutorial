users = [
    {
        "Name":"alvin",
        "Password":"12345"
    },
    {
        "Name":"alex",
        "Password":"98276"
    },
    {
        "Name":"ivy",
        "Password":"83932"
    },
    {
        "Name":"allen",
        "Password":"82820"
    }
]

name = "Ivy"
password = "83932"

for data in users:
    name =  name.lower()
    if name == data["Name"]:
        print("Name found")
        if password == data["Password"]:
           print("You have logged in succesfully")
           break
        else:
           print("You've entered the wrong password or name")
    else:
        print(f"Name {name} not found")

        

