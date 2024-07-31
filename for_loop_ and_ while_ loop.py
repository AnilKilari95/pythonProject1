#Sum of Numbers: Write a program that calculates the
# sum of all numbers from 1 to n, where n is provided by the user.
#n = int(input("enter n number"))
#sum = 0
#for i in range(1,n+1):
 #   sum = sum + i
#print(sum)

#Factorial Calculation: Write a program that calculates the
# factorial of a given number n provided by the user.
n = int(input("enter n number"))
ft = 1
i = 0;
for i in range(n,1,-1):
    ft = ft * i
print(ft)

#Reverse a String: Write a program that reverses a given string.
s = "hello"
print(s[::-1])

#Count Vowels in a String: Write a program that counts the number of vowels in a given string.
s = "hello"
vol = ["a","e","i","o","u"]
count = 0
for i in s:
    if i in vol:
        count = count + 1
print(count)

#Print Multiplication Table: Write a program that prints the multiplication table of a given number n.
mul = 1
n = int(input("enter n value"))
for i in range(1,11):
    mul = n * i
    print(n,"*",i ,"=", mul)


#Check for Prime Number: Write a program that checks whether a given number n is prime.
n = int(input("enter n value"))
p = 0
for i in range(2,(n//2)+1):
    if n % i == 0:
        p = p+1
        break
if p == 0 and n!=1:
    print("prime")
else:
    print("not a prime")


#Fibonacci Series: Write a program that generates the Fibonacci series
#up to the nth term, where n is provided by the user.
n = int(input("Enter the number of terms: "))
a, b = 0, 1
print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

#Count Digits in a Number: Write a program that counts the number of digits in a given number.
n = input("Enter n value: ")
count = 0
for i in n:
    if i.isdigit():
        count = count+1
print(count)














