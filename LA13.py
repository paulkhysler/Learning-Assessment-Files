print("=== LEARNING ACTIVITY 13: LOOP PRACTICE ===")

print("\nPart A: For Loop")

print("\n1) Numbers 1 to 10:")
for number in range(1, 11):
	print(number)

print("\n2) Even numbers from 2 to 20:")
for even in range(2, 21, 2):
	print(even)

print("\n3) Items in a list with their index:")
items = ["Notebook", "Pen", "Bag", "Calculator", "ID"]
for index, item in enumerate(items):
	print(f"Index {index}: {item}")

print("\nPart B: While Loop")

print("\n4) Countdown from 10 to 1:")
count = 10
while count >= 1:
	print(count)
	count -= 1
print("Blast off!")

print("\n5) Guessing Game")
secret_number = 6
guess = None

while guess != secret_number:
	guess = int(input("Guess the number (1-10): "))
	if guess < secret_number:
		print("Too low. Try again.")
	elif guess > secret_number:
		print("Too high. Try again.")
	else:
		print("Correct! You guessed the number.")
