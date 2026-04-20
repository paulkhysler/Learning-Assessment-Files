# GRADE CALCULATOR

score_input = input("Enter your numeric score (0-100): ")
score = float(score_input)

if score < 0 or score > 100:
    print("Invalid score. Please enter a value from 0 to 100.")
else:
    if score >= 90:
        grade = "A"
        message = "Excellent!"
    elif score >= 80:
        grade = "B"
        message = "Very Good!"
    elif score >= 70:
        grade = "C"
        message = "Good."
    elif score >= 60:
        grade = "D"
        message = "Needs Improvement."
    else:
        grade = "F"
        message = "Failed."
    print(f"Score: {score:.0f} -> Grade: {grade} - {message}")
