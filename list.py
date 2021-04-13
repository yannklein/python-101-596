students = ["Noza", "Adrien", "Phil"]
#             0       1         2
print(students)
print(students[:2])
print(students[1:2])

print(len(students))

print("Adrien" in students)
print("Tomo" in students)

# CRUD

# Create
students.append("Yutaka")
print(students)

# Read
print(students[1])

# Update
students[2] = 'Super Phil'
print(students)
# Delete
del students[2]
print(students)


# for student in students:
#     print(f"{student} is amazing!")


[ print(f"{student} is amazing!") for student in students]

new_students = [ f"{student} is amazing!" for student in students]
print(new_students)

for index, student in enumerate(students):
    print(f"{index + 1} - {student} is amazing!")








