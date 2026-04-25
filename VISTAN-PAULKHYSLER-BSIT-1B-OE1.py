# Movie Ticket System

print("=== MOVIE TICKET SYSTEM ===")

# Part A: Get user inputs
day = input("Day (weekday/weekend): ").strip().lower()
customer_type = input("Customer type (regular/student/senior): ").strip().lower()
show_time = int(input("Show time (hour in 24-hour format): "))
num_tickets = int(input("Number of tickets: "))

# Part D: Validate inputs
if show_time < 9 or show_time > 22:
    print("Error: Show time must be between 9 and 22.")
elif num_tickets <= 0:
    print("Error: Number of tickets must be positive.")
else:
    # Part B: Base pricing
    if day == "weekday":
        base_price = 200.0
    elif day == "weekend":
        base_price = 300.0
    else:
        print("Error: Day must be 'weekday' or 'weekend'.")
        exit()

    base_total = base_price * num_tickets

    # Part C: Discounts (nested conditionals)
    student_discount = 0.0
    senior_discount = 0.0
    matinee_discount = 0.0
    group_discount = 0.0

    # Customer type discounts
    if customer_type == "student":
        student_discount = 0.20 * base_total
    elif customer_type == "senior":
        senior_discount = 0.30 * base_total
    elif customer_type != "regular":
        print("Error: Customer type must be regular/student/senior.")
        exit()

    # Matinee discount (before 12pm)
    if show_time < 12:
        matinee_discount = 0.10 * base_total

    # Group discount (5+ tickets)
    if num_tickets >= 5:
        group_discount = 0.05 * base_total

    total_discount = student_discount + senior_discount + matinee_discount + group_discount
    final_total = base_total - total_discount

    # Part E: Display itemized receipt
    print("\n--- RECEIPT ---")
    print(f"Day: {day}")
    print(f"Customer type: {customer_type}")
    print(f"Show time: {show_time}")
    print(f"Number of tickets: {num_tickets}\n")

    print(f"Base price: {base_price:.2f} x {num_tickets} = {base_total:.2f}")
    if student_discount > 0:
        print(f"Student discount (20%): -{student_discount:.2f}")
    if senior_discount > 0:
        print(f"Senior discount (30%): -{senior_discount:.2f}")
    if matinee_discount > 0:
        print(f"Matinee discount (10%): -{matinee_discount:.2f}")
    if group_discount > 0:
        print(f"Group discount (5%): -{group_discount:.2f}")

    print(f"\nTOTAL: {final_total:.2f}")
    print("Thank you for your purchase!")
