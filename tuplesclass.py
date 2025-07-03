students = (
    ("Aarav", 12, (85, 90, 78)),
    ("Diya", 11, (92, 88, 95)),
    ("Kabir", 13, (76, 70, 80)),
    ("Riya", 12, (89, 85, 91))
)


print("Students who scored more than 85 in all subjects:")
for student in students:
    name,age,marks=student
    if all(mark > 85 for mark in marks):
        print(name)

for student in students:
    name,age,marks=student
    average = sum (marks) /3
    print(name , average)

toppername = ""
toppertotal=0

for student in students:
    name,age,marks=student
    total = sum(marks)
    if total > toppertotal:
        toppertotal=total
        toppername=name

print(toppername, "is the topper") 