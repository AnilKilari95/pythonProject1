x = 5
y = "Hello"
print(type(x))
print(type(y))

#How do you create a list in Python? Create a list of numbers from 1 to 5.
l=[1,2,3,4,5]
print(l)

#What is the difference between a list and a tuple in Python? Create a tuple containing
# the names "Alice", "Bob", and "Charlie".
l=["Alice","Bob","Charlie"]
l1=("Alice","Bob","Charlie")
print(l)
print(l1)

#How do you create a dictionary in Python?
# Create a dictionary with keys "name", "age", and "city" with appropriate values.
d={"name":"k","age":1,"city":"T"}
print(d)

# output of the following code
s = "Hello, World!"
print(s[7:])

#How do you convert an integer to a float in Python? Convert the integer 7 to a float.
i=int(7)
i1=float(i)
print(i1)

#What are the possible values for a boolean data type in Python?
a=True
b=False
print(type(a))
print(type(b))

#basic arithmetic operations
a = 10
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)

#How do you convert a string to uppercase in Python? Convert the string "hello" to uppercase.
s="hello"
s1=s.upper()
print(s1)

#Given the list my_list = [10, 20, 30, 40, 50],
# how do you access the element at index 2? What will be the output?
my_list=[10,20,30,40,50]
print(my_list[2])

#How do you access the value associated with the key "age" in the following dictionary?
person = {"name": "John", "age": 30, "city": "New York"}
person["age"]

#How do you find the length of a list in Python?
# Find the length of the list [1, 2, 3, 4, 5].
l=[1,2,3,4,5]
print(len(l))

#String Concatenation
#How do you concatenate two strings in Python?
#Concatenate the strings "Hello" and "World" with a space in between.
l="Hello "
l2="World"
l3=l+l2
print(l3)

'''List Slicing

What will be the output of the following code?'''

my_list = [1, 2, 3, 4, 5]
print(my_list[1:4])

#Updating Lists
#How do you add an element to the end of a list in Python?
#Add the number 6 to the list [1, 2, 3, 4, 5].
l=[1,2,3,4,5]
l.append(6)
print(l)

#Basic Arithmetic:

#How do you add two numbers in Python?
a=1
b=2
c=a+b
print(c)
#How do you subtract one number from another in Python?
a=2
b=1
c=a-b
print(c)
#How do you multiply two numbers in Python?
a=1
b=2
c=a*b
print(c)
#How do you divide one number by another in Python?
a=4
b=2
c=a/b
print(c)
#How do you find the remainder of the division of two numbers in Python?
a=1
b=2
c=a%b
print(c)

a=1
b=2
c=a//b
print(c)

#Variable Assignment:
#How do you assign the value 10 to a variable named x in Python?
x=10
print(x)
#How do you assign the value 3.14 to a variable named pi in Python?
pi=3.14
print(pi)

#String Operations:
#How do you concatenate two strings "Hello" and "World" in Python?
l="Hello"
l1=" World"
l2=l+l1
print(l2)
#How do you find the length of a string "Python" in Python?
l="Python"
print((len(l)))
#How do you convert the string "123" to an integer in Python?
s="123"
i=int(s)
print(i)

#Lists:
#How do you create a list containing the numbers 1, 2, and 3 in Python?
l=[1,2,3]
print(l)
#How do you add the number 4 to the end of a list in Python?
l.append(4)
print(l)
#How do you remove the number 2 from a list in Python?
l.remove(2)
print(l)
l.pop()
print(l)
l.pop(0)
print(l)

#Loops:
#How do you write a for loop that prints numbers from 1 to 5 in Python?
for i in range(1,6):
    print(i)
#How do you write a while loop that prints numbers from 1 to 5 in Python?
i=1;
while(i<=5):
    print(i)
    i=i+1

#Conditional Statements:
#How do you write an if statement that checks if a variable x is greater than 10 in Python?
x=20
if x > 10:
    print(True)
else:
    print(False)

def check_number(x):
    if x > 10:
        return True
    else:
        return False
y=check_number(5)
print(y)



#Functions:
#How do you define a function named add that takes two parameters and returns their sum in Python?
def add(a,b):
    return a+b
c=add(2,3)
print(c)







#How do you call a function named greet with the argument "Alice" in Python?
def greet(x):
    return x
y=greet("Alice")
print(y)



#How do you write an if-else statement that prints "Yes" if a variable y is less than 5 and "No" otherwise in Python?
y = 5
if y < 5:
    print("yes")
else:
    print("no")

num = int(input("enter any number "))
if num < 5:
    print("yes")
else:
    print("no")


#Dictionaries:
#How do you create a dictionary with keys "name" and "age" and
# corresponding values "Alice" and 25 in Python?
d={"name":"Alice","age":25}
print(d)
#How do you access the value associated with the key "name" in a dictionary in Python?
c=d["name"]
print(c)