# Program 1
from datetime import datetime
name = input("Enter your name: ")
year_of_birth = int(input("Enter your year of birth: "))
current_year = datetime.now().year
age = current_year - year_of_birth
print(f"Hello, {name}! You are {age} years old.")

# Program 2
txt = 'LMaasleitbtui'
cars = txt[::2]
print(f"Car names: {cars}")

# Program 3
user_string = input("Enter a string: ")
print(f"Length of the string: {len(user_string)}")
print(f"Uppercase: {user_string.upper()}")
print(f"Lowercase: {user_string.lower()}")

# Program 4
user_string = input("Enter a string: ")
if user_string == user_string[::-1]:
    print(f"'{user_string}' is a palindrome.")
else:
    print(f"'{user_string}' is not a palindrome.")

# Program 5
user_string = input("Enter a string: ").lower()
vowels = "aeiou"
vowel_count = sum(1 for char in user_string if char in vowels)
consonant_count = sum(1 for char in user_string if char.isalpha() and char not in vowels)
print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")

# Program 6
string1 = input("Enter the main string: ")
string2 = input("Enter the string to search for: ")
if string2 in string1:
    print(f"'{string2}' is found in '{string1}'.")
else:
    print(f"'{string2}' is not found in '{string1}'.")

# Program 7
sentence = input("Enter a sentence: ")
word_to_replace = input("Enter the word to replace: ")
replacement = input("Enter the replacement word: ")
updated_sentence = sentence.replace(word_to_replace, replacement)
print(f"Updated sentence: {updated_sentence}")

# Program 8
user_string = input("Enter a string: ")
print(f"First character: {user_string[0]}")
print(f"Last character: {user_string[-1]}")

# Program 9
user_string = input("Enter a string: ")
reversed_string = user_string[::-1]
print(f"Reversed string: {reversed_string}")

# Program 10
sentence = input("Enter a sentence: ")
word_count = len(sentence.split())
print(f"Number of words: {word_count}")

# Program 11
user_string = input("Enter a string: ")
if any(char.isdigit() for char in user_string):
    print("The string contains digits.")
else:
    print("The string does not contain any digits.")

# Program 12
words = input("Enter words separated by spaces: ").split()
separator = input("Enter a separator: ")
joined_string = separator.join(words)
print(f"Joined string: {joined_string}")

# Program 13
user_string = input("Enter a string: ")
no_spaces = user_string.replace(" ", "")
print(f"String without spaces: {no_spaces}")

# Program 14
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
if string1 == string2:
    print("The strings are equal.")
else:
    print("The strings are not equal.")

# Program 15
sentence = input("Enter a sentence: ")
acronym = "".join(word[0].upper() for word in sentence.split())
print(f"Acronym: {acronym}")

# Program 16
user_string = input("Enter a string: ")
char_to_remove = input("Enter the character to remove: ")
result = user_string.replace(char_to_remove, "")
print(f"String after removal: {result}")

# Program 17
user_string = input("Enter a string: ")
symbol = input("Enter a symbol to replace vowels with: ")
vowels = "aeiouAEIOU"
result = "".join(symbol if char in vowels else char for char in user_string)
print(f"String after replacing vowels: {result}")

# Program 18
user_string = input("Enter a string: ")
start_word = input("Enter the starting word: ")
end_word = input("Enter the ending word: ")
starts_with = user_string.startswith(start_word)
ends_with = user_string.endswith(end_word)
print(f"Starts with '{start_word}': {starts_with}")
print(f"Ends with '{end_word}': {ends_with}")
