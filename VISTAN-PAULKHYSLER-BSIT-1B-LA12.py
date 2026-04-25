gradebook = [
	["Aaron", 88, 91, 85],
	["Prix", 90, 87, 92],
	["Reymart", 84, 89, 86],
	["Fabi", 93, 90, 94]
]

print("1. Entire gradebook:")
print(gradebook)

second_student_quiz2 = gradebook[1][2]
print("\n2. 2nd student's quiz2 score:", second_student_quiz2)

gradebook[2][1] = 100
print("\n3. After updating 3rd student's quiz1 score to 100:")
print(gradebook)

gradebook.append(["Aisha", 85, 88, 90])
print("\n4. After adding a new student row:")
print(gradebook)

print("\n5. Updated gradebook:")
print(gradebook)
