student = {
  'name': 'Tomo',
  'age': 21,
  'nationality': "Japenese"
}

print(student)


# useful fonction on dict
print(len(student))
print('name' in student)
print('job' in student)
print('Tomo' in student)
print(student.keys())
print(list(student.keys())[0])
print(student.values())
print(student.items())

#CRUD

# Create
student['hobby'] = 'surfing'
print(student)

# Read
print(student['age'])

# Update
student['nationality'] = 'French'
print(student)

# Delete
del student['nationality']
print(student)


print(student.get('job', 'Not found!!'))

for key, value in student.items():
    print(f"Key is {key} and value is {value}.")





