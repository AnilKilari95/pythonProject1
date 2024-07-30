# print 1 to 5 numbers using whileloop
i=1
while (i<=5):
    print(i)
    i=i+1
#sum of the first n natural numbers using whileloop
n=10
sum=0
i=1;
while(i<=n):
    sum=sum+i
    i=i+1
print(sum)
#break at 5
i=1
while (i<=10):
    print(i)
    if i==5:
        break
    i = i + 1
# break the loop
while True:
    print("This will run forever unless stopped manually!")
    break
#Try writing a while loop that asks the user to input a number and prints the square of that number.
# The loop should stop if the user inputs a negative number.
#while True:
 #   no = int(input("enter any number "))
  #  if (no < 0):
   #     break
    #z = no**2
    #print(z)

#list comprehension  [expression for item in iterable if condition]
#Create a list of squares of numbers from 0 to 9.
squares = [x**2 for x in range(10)]
print(squares)
#With a Condition:
#Create a list of even numbers from 0 to 9.
even_nums=[i for i in range(10) if i%2==0]
print(even_nums)

#Convert a list of strings to uppercase.
words = ["hello", "world", "python"]
uppercase_words = [word.upper()for word in words]
print(uppercase_words)

#2D list matrix
matrix = [[i + j for j in range(3)] for i in range(3)]
print(matrix)
mat=[[i+j for i in range(3)] for j in range(3)]
print(mat)

#lambda arguments: expression
# A lambda function that adds 10 to the input
add_ten = lambda x: x + 10
print(add_ten(5))

# A lambda function that multiplies two numbers
multiply = lambda x, y: x * y
print(multiply(2, 3))

# Using lambda with map to square each number in a list
numbers = [1, 2, 3, 4]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)

# Using lambda with filter to get even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# Sorting a list of tuples by the second value
tuples = [(1, 'd'), (2, 'b'), (3, 'a'), (4, 'c')]
sorted_tuples = sorted(tuples, key=lambda x: x[1])
print(sorted_tuples)


#Write a while loop that prints the numbers from 1 to 10.
i=1;
while i<11:
    print(i)
    i=i+1

#Write a while loop that prints the even numbers between 1 and 20.
i=2;
while i<=20:
    print(i)
    i=i+2

#Write a while loop that prints the numbers from 10 to 1 in reverse order.
i=10;
while i>0:
    print(i)
    i=i-1

#Write a while loop that calculates and prints the sum of the first 10 natural numbers.
n=10
i=1;
sum=0
while (i<=n):
    sum=sum+i
    i=i+1
print(sum)

#Write a while loop that prints the Fibonacci sequence up to the 10th term.
# Initialize the first two terms
a, b = 0, 1
count = 1

# We want to print the first 10 terms
while count <= 10:
    print(a)
    # Update the values of a and b
    a, b = b, a + b
    count += 1



#Write a simple while loop that prints numbers from 1 to 5.
i=1;
while (i<=5):
    print(i)
    i=i+1

#What is an infinite loop, and how can you create one using a while loop?
#Explain the purpose of the break statement in a while loop.
i = 1;
while i < 5:
    i = i + 1
    print("a", i)
    if i == 4:
        print(i)
    else:
        break

#Write a Python program that keeps asking the user to enter a number.
# If the user enters a negative number, the program should stop asking for more numbers and print
# "Negative number entered, exiting the loop." Otherwise, it should keep asking for a new number.
while True:
    num = int(input("enter any number"))
    if num < 0:
        print(num)
        break
    else:
        print(num)

'''Write a Python program that asks the user to guess a predefined secret number (e.g., 42). 
The program should keep asking the user for a guess until they get it right. 
If the user guesses the secret number correctly, 
the program should print "Congratulations! You've guessed the secret number!" and exit the loop.'''
n = 42;
while True:
    num = int(input("guess the secret number"))
    if num == n:
        print("Congratulations! You've guessed the secret number!")
        break
    else:
        print("Incorrect, try again!")

#Write a while loop that prints the numbers from 1 to 10, but skips the number 5.
i = 1;
while i <= 10:
    if i== 5:
        i = i+1
        continue
    print(i)
    i=i+1

#Write a while loop to sum the numbers from 1 to 100.
i = 1;
sum = 0
while i <= 100:
    sum=sum+i
    i=i+1
print(sum)

#Write a while loop that takes user input and continues to ask for input until the user types "exit".
while True:
    num = input("ask for input")
    if num == "exit":
        print("exit")
        break
    else:
        print(num)

#Print all even numbers between 1 and 20 using a while loop.
i = 2;
while i <= 20:
    if i % 2 == 0:
        print(i)
        i=i+2

#Use a while loop to reverse a given string
x = "Hello"
y = ""
i = len(x) - 1
while i >= 0:
    y += x[i]
    i -= 1
    print(y)


# Given string
input_string = "hello"
reversed_string = ""
index = len(input_string) - 1
while index >= 0:
    reversed_string += input_string[index]
    index -= 1
print("Reversed string:", reversed_string)

#Create a while loop that prints the Fibonacci sequence up to a specified number.
# Specify the maximum number up to which to generate the Fibonacci sequence
max_number = 100
a, b = 0, 1
print(max_number, ":")
while a <= max_number:
    print(a, end=" ")
    a, b = b, a + b

#Write a while loop to find the factorial of a given number.
ft =1
no = int(input("enter any number"))
i =1;
while i <= no:
    ft = ft * i
    i = i + 1
    print(ft)





















