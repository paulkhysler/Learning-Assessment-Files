# Username Generator Program

full_name = input("Enter your full name: ")
birth_year = input("Enter your birth year: ")

name_parts = full_name.strip().split()
if len(name_parts) < 2:
    print("Error: Please enter both first and last name.")
else:
    first_name = name_parts[0]
    last_name = name_parts[-1]
    
    # Generate username following the rules:
    # - First 3 letters of first name (lowercase)
    # - First 3 letters of last name (lowercase)
    # - Last 2 digits of birth year
    username = first_name[:3].lower() + last_name[:3].lower() + birth_year[-2:]
    
    print(f"\nGenerated username: {username}")
