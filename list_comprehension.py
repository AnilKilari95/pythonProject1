#Write a list comprehension to create a list of squares of numbers from 1 to 10
l = [i * i for i in range(1, 11)]
print(l)

#Even Numbers Filter
#Given a list of numbers, write a list comprehension to
#create a new list containing only the even numbers.
numbers = [1,2,3,4,5,6,7,8,9,10]
l = [i for i in numbers if i % 2 == 0]
print(l)

'''Uppercase Strings
Given a list of strings, use a list comprehension to 
create a new list with each string converted to uppercase.'''
words = ['hello', 'world', 'python', 'programming']
l = [word.upper() for word in words]
print(l)

#Length of Strings
#Write a list comprehension to create a list of the lengths of each string in a list.
words = ['apple', 'banana', 'cherry', 'date']
l =[len(word) for word in words]
print(l)

#Multiples of Three
#Create a list of numbers from 1 to 20 that are multiples of 3.
l =[i for i in range(1,21) if i%3 == 0]
print(l)

#Flatten a List of Lists
#Given a list of lists, use a list comprehension to flatten it into a single list.
list_of_lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
l = [item for sublist in list_of_lists for item in sublist]
print(l)

#Conditional Expression
'''Given a list of integers, create a new list where each element is
squared if it is even and cubed if it is odd.'''
numbers = [1, 2, 3, 4, 5]
new_list = [i**2 if i % 2 == 0 else i**3 for i in numbers ]
print(new_list)

#Extracting Digits
#Write a list comprehension to extract all the digits from a string.
text = "hello123world456"
digits =[i for i in text if i.isdigit()]
print(digits)

#Prime Numbers
#Use a list comprehension to find all prime numbers between 1 and 50.
primes = [num for num in range(2, 51) if all(num % i != 0 for i in range(2, int(num**0.5) + 1))]
print(primes)

#Fahrenheit to Celsius Conversion
#Given a list of temperatures in Fahrenheit, use a list comprehension to convert them to Celsius.
fahrenheit = [32, 68, 104, 212]
celsius = [(temp - 32) * 5/9 for temp in fahrenheit]
print(celsius)