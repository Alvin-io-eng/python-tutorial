students = ["Hermione","Harry","Ron"]

print(students[0])
print(students[1])
print(students[2])

for student in students:
    print(student)

for _ in students:
    print(_)

for i in range(len(students)):
    print(students[i])

for i in range(len(students)):
    print(i, students[i])

for i in range(len(students)):
    print(i + 1, students[i])\
    
for i in range(len(students)):
    print(i + 1, students[i])