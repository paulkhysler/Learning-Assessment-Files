# Student ID Card Generator
# This program generates a formatted student ID card

# Collect student information
full_name = input("Enter full name: ").strip()
course_code = input("Enter course code: ").strip()
year_level = int(input("Enter year level (1-4): ").strip())
birth_date = input("Enter birth date (MM/DD/YYYY): ").strip()

# Process the data
name_parts = full_name.split()
last_name = name_parts[-1]
formatted_name = full_name.title()
course_upper = course_code.upper()
birth_year = birth_date.split('/')[-1]

# Convert year level to ordinal format
year_suffix = {1: "1st Year", 2: "2nd Year", 3: "3rd Year", 4: "4th Year"}
year_text = year_suffix.get(year_level, f"{year_level}th Year")

# Generate student ID: COURSE-YEAR-LASTNAME-BIRTHYEAR
student_id = f"{course_upper}-{year_level}-{last_name.upper()}-{birth_year}"

# Display the ID card
print("\n" + "=" * 60)
print("║" + " " * 58 + "║")
print("║" + "STUDENT ID CARD".center(58) + "║")
print("║" + " " * 58 + "║")
print("║" + "─" * 58 + "║")
print("║" + " " * 58 + "║")
print("║" + f"  Name:".ljust(20) + formatted_name.ljust(38) + "║")
print("║" + f"  Course:".ljust(20) + course_upper.ljust(38) + "║")
print("║" + f"  Year:".ljust(20) + year_text.ljust(38) + "║")
print("║" + " " * 58 + "║")
print("║" + f"  Student ID: {student_id}".ljust(58) + "║")
print("║" + " " * 58 + "║")
print("=" * 60)

print("\nID Generated Successfully!")
