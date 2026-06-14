char = input("Enter a single character: ")

# Ensure the input is a single alphabet character
if len(char) == 1 and char.isalpha():
    if char.lower() in ['a', 'e', 'i', 'o', 'u']:
        print(f"'{char}' is a vowel.")
    else:
        print(f"'{char}' is not a vowel.")
else:
    print("Invalid input! Please enter a single alphabetical character.")