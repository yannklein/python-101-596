age = int(input("How old are you? "))

# Add one year to age => re-assignement
age += 1

# concatenation
sentence = "Next year, you will be " + str(age) + " years-old"

# interpolation
sentence = f"Next year, you will be {age} years-old"

print(sentence)
