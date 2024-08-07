# Write a Python function to reverse a string.
s = "hello"
print(s[::-1])

#How would you check if a string is a palindrome?
def is_palindrome(input_string):
    return input_string == input_string[::-1]
print(is_palindrome("racecar"))
print(is_palindrome("hello"))

#Write a function that takes a string and returns the number of vowels in it.
def count_vowels(input_string):
    return sum(char in "aeiouAEIOU" for char in input_string)
print(count_vowels("hello"))
print(count_vowels("hello,world"))

#How can you remove all occurrences of a given character from a string?
def remove_char(input_string, char_to_remove):
    return input_string.replace(char_to_remove, "")

print(remove_char("hello","l"))


#Write a Python function that capitalizes the first letter of each word in a string.
s = "hello world"
x = s.title()
print(x)

#How do you find the first non-repeating character in a string?
def first_non_repeating_char(input_string):
    for char in input_string:
        if input_string.count(char) == 1:
            return char
    return None

print(first_non_repeating_char("hello"))
print(first_non_repeating_char("aabbcc"))

#Write a function to check if two strings are anagrams.
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)
print(are_anagrams("listen", "silent"))
print(are_anagrams("hello", "world"))

#How would you replace all spaces in a string with underscores?
s = "hello world where are you"
x = s.replace(" ", "_")
print(x)
#Write a Python function that counts the number of words in a string.
s = "hello, world"
x = len(s.split())
print(x)

#How can you extract all the digits from a string?
def extract_digits(input_string):
    return ''.join(i for i in input_string if i.isdigit())
print(extract_digits("hello 123 world 456"))
print(extract_digits("abc123xyz456"))

#Write a function to convert a string to lowercase without using built-in methods.
def to_lowercase(input_string):
    result = []
    for char in input_string:
        if 'A' <= char <= 'Z':
            result.append(chr(ord(char) + 32))
        else:
            result.append(char)
    return ''.join(result)
print(to_lowercase("Hello World"))
print(to_lowercase("PYTHON"))

#Write a Python function to remove leading and trailing whitespace from a string.
s = " hello,world,india  "
print(s.strip())

#Write a function to find the frequency of each character in a string.
def character_frequency(input_string):
    frequency = {}
    for char in input_string:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency
print(character_frequency("hello"))
print(character_frequency("abcabc"))


#How do you check if a string contains only alphabets?
s = "hello"
print(s.isalpha())
t = "hello123"
print(t.isalpha())

#Write a Python function that swaps the cases of all letters in a string.
s = "HELLO world"
print(s.swapcase())
#How would you count the number of uppercase and lowercase letters in a string?
def count_upper_lower(input_string):
    upper_count = 0
    lower_count = 0

    for char in input_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count
s = "HELLO world"
upper_count, lower_count = count_upper_lower(s)
print(f"Uppercase letters: {upper_count}")
print(f"Lowercase letters: {lower_count}")

#Write a function to check if a string starts with a specified prefix.
s = "hello world"
x = s.startswith("hello")
print(x)

#How can you concatenate two strings without using the + operator?
x = "hello"
y = "world"
z = " ".join((x,y))
print(z)