students = ["Prix", "Aaron", "Erjohn", "Mizzy", "Aisha"]
print("1. Initial list:", students)

students.append("Fabi")
students.insert(2, "Reymart")
print("2. After append and insert:", students)

students[2] = "Paul"
print("3. After updating 3rd student to your name:", students)

students.remove("Mizzy")
print("4. After remove('Mizzy'):", students)

removed_student = students.pop()
print("5. Popped last student:", removed_student)
print("   List after pop:", students)

print("6. Final list:", students)
print("   Length of final list:", len(students))
