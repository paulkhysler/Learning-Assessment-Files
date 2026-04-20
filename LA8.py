# Text Processor Program

sentence = input("Enter a sentence: ")

print("\n--- Text Processor Results ---\n")

print(f"Uppercase: {sentence.upper()}")
print(f"Lowercase: {sentence.lower()}")
print(f"Title Case: {sentence.title()}")

count_a = sentence.lower().count('a')
print(f"\nCount of letter 'a' (case-insensitive): {count_a}")

stripped = sentence.strip()
print(f"\nAfter removing leading/trailing spaces: '{stripped}'")

underscored = sentence.replace(' ', '_')
print(f"\nSpaces replaced with underscores: {underscored}")

print("\nWords on separate lines:")
words = sentence.split()
for word in words:
    print(word)
