#### Q-24  / WAP to input a charecter and tell the type of the vowel

char = input("Enter a character: ")

# Convert the character to lowercase (to handle both uppercase and lowercase input)
char_lower = char.lower()

# Check if it is a vowel and its type
if char_lower == 'a':
    print("It is a lowercase vowel 'a'.")
elif char_lower == 'e':
    print("It is a lowercase vowel 'e'.")
elif char_lower == 'i':
    print("It is a lowercase vowel 'i'.")
elif char_lower == 'o':
    print("It is a lowercase vowel 'o'.")
elif char_lower == 'u':
    print("It is a lowercase vowel 'u'.")
elif char.isalpha():       # check the alpha numeric charectar
    print("It is a consonant.")
else:
    print("Invalid input.")