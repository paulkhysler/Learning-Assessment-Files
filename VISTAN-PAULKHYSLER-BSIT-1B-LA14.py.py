print("=== LEARNING ACTIVITY 14 ===")

matrix = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]

print("\n1) 3x3 Matrix:")
for row in matrix:
	print(row)

print("\n2) Matrix row by row (nested loops):")
for row in matrix:
	for value in row:
		print(value, end=" ")
	print()

print("\n3) Sum of each row:")
row_number = 1
for row in matrix:
	row_sum = 0
	for value in row:
		row_sum += value
	print(f"Row {row_number} sum = {row_sum}")
	row_number += 1

print("\n4) Sum of each column:")
for column_index in range(3):
	column_sum = 0
	for row_index in range(3):
		column_sum += matrix[row_index][column_index]
	print(f"Column {column_index + 1} sum = {column_sum}")

print("\n5) Diagonal elements:")
diagonal_elements = []
for index in range(3):
	diagonal_elements.append(matrix[index][index])
print(diagonal_elements)

print("\n6) 5-row right triangle star pattern:")
for row in range(1, 6):
	print("*" * row)
