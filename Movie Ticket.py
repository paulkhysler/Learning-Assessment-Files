print("=== MOVIE TICKET SYSTEM ===")

# Inputs
day = input("Day (weekday/weekend): ").lower()
customer_type = input("Customer type (regular/student/senior): ").lower()
show_time = int(input("Show time (hour in 24-hour format): "))
num_tickets = int(input("Number of tickets: "))

# Validate time
if show_time < 9 or show_time > 22:
    print("Error: Show time must be between 9 and 22.")
# Validate tickets
elif num_tickets <= 0:
    print("Error: Number of tickets must be positive.")
# Validate day
elif day != "weekday" and day != "weekend":
    print("Error: Day must be 'weekday' or 'weekend'.")
# Validate customer type
elif customer_type != "regular" and customer_type != "student" and customer_type != "senior":
    print("Error: Customer type must be regular/student/senior.")
else:
    # Base price
    if day == "weekday":
        base_price = 200
    else:
        base_price = 300

    base_total = base_price * num_tickets

    # Start with no discount
    discount = 0

    # Customer discounts
    if customer_type == "student":
        discount = discount + (0.20 * base_total)
    elif customer_type == "senior":
        discount = discount + (0.30 * base_total)

    # Matinee discount (before 12)
    if show_time < 12:
        discount = discount + (0.10 * base_total)

    # Group discount (5 or more tickets)
    if num_tickets >= 5:
        discount = discount + (0.05 * base_total)

    final_total = base_total - discount

    print("\n--- RECEIPT ---")
    print("Day:", day)
    print("Customer type:", customer_type)
    print("Show time:", show_time)
    print("Number of tickets:", num_tickets)
    print()
    print("Base price:", base_price, "x", num_tickets, "=", base_total)
    print("Total discount: -", round(discount, 2))
    print("TOTAL:", round(final_total, 2))
    print("Thank you for your purchase!")
