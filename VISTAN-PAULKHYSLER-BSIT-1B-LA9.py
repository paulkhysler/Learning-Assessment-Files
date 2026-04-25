# Receipt Generator Program

item_name = input("Enter item name: ")
quantity = int(input("Enter quantity: "))
unit_price = float(input("Enter unit price: "))

total = quantity * unit_price

print("\n" + "=" * 60)
print("RECEIPT".center(60))
print("=" * 60)
print(f"{'Item':<15}{'Qty':>5}{'Unit Price':>15}{'Amount':>15}")
print("-" * 60)
print(f"{item_name:<15}{quantity:>5}{unit_price:>15,.2f}{total:>15,.2f}")
print("-" * 60)
print(f"{'TOTAL':<35}{total:>15,.2f}")
print("=" * 60)
