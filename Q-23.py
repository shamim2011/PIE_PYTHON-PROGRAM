#### Q-23  / WAP to input a charecter and check weather it is a vowel or consonant

char = input("Enter a character: ")

# Convert the character to lowercase (to handle both uppercase and lowercase input)
char = char.lower()

# Check if it is a vowel or consonant
if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
    print("It is a vowel.")
else:
    print("It is a consonant.")