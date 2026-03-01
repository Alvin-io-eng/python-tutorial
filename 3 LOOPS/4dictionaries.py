prevStudents = ["Hermione","Harry","Ron","Draco"]
houses = ["Griffindor","Griffindor","Griffindor","Slytherin"]

# Dictionary

preStudents = {
    "Hermione":"Griffindor",
    "Harry":"Griffindor",
    "Ron":"Griffindor",
    "Draco":"Slytherin"
    }

print(preStudents["Hermione"])

for student in preStudents:
    print(student, preStudents[student], sep=", ")
    # print(student + ", " + preStudents[student])

# for i in range(len(preStudents)):
#     print(i)

students = [
    {"Name" : "Herminoe", "House" : "Grifindor", "Patronus" : "Otter"},
    {"Name" : "Harry", "House" : "Grifindor", "Patronus" : "Stag"},
    {"Name" : "Ron", "House" : "Grifindor", "Patronus" : "Jack Russell Terrier"},
    {"Name" : "Draco", "House" : "Slytherin", "Patronus" : None},
]

for student in students:
    print(student["Name"],student["House"],student["Patronus"],sep=", ")