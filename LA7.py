name = input("Enter your full name: ")

print(f"\nFirst character: {name[0]}")
print(f"Last character: {name[-1]}")
print(f"First 5 characters: {name[:5]}")
print(f"Name in reverse: {name[::-1]}")
print(f"Every other character: {name[::2]}")

name_length = len(name)
if name_length % 2 == 1:
    middle_index = name_length // 2
    print(f"Middle character: {name[middle_index]}")
else:
    middle_index = name_length // 2
    print(f"Middle characters: {name[middle_index-1:middle_index+1]}")
