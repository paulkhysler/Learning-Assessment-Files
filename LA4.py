# ELIGIBILITY CHECKER

age = int(input("Please enter your age: "))
has_valid_id = input("Do you have a valid ID? (yes/no): ").lower()

if age >= 18 and has_valid_id == "yes":
    if age >= 60:
        print("Eligible! (Senior discount applies)")
    else:
        print("Eligible!")
else:
    print("Not eligible")
    
    if age < 18 and not has_valid_id == "yes":
        print("Reason: Must be 18 or older AND have a valid ID")
    elif age < 18:
        print("Reason: Must be 18 or older")
    elif not has_valid_id == "yes":
        print("Reason: Must have a valid ID")
