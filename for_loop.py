# Write a program to print numbers from 1 to 10 using a for loop.
for i in range(1,11):
    print(i)
print("completed")



# Write a program to calculate the sum of the first 10 natural numbers (1 to 10).
sum=0
for i in range(1,11):
    sum=i+sum
print(sum)
print("completed")

# Write a program to print all even numbers from 1 to 20 using a for loop.
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
print("completed")

# Write a program to print the multiplication table of 5 using a for loop.
table=5
for i in range(1,11):
    t=i*table
    print(table, "*" ,i ,"=",  t)
print("completed")

# Write a program to reverse a string using a for loop.
a="Hello"
print(a[0:2])
print(a[::-1])
print(a[-1:-6:-1])
print("completed")

# Write a program to find the factorial of a given number using a for loop.
#ft=1
#no=int(input("enter any number"))
#for i in range(no,0,-1):
 #   ft=ft*i
#print(ft)
#ptint("completed")


#Write a program to print all elements of a list using a for loop.
l = [1, 2, 3, 4, 5]
for i in l:
    print(i)
print("completed")

# Write a program to count the number of vowels in a given string using a for loop.
v="HelloWorld"
vowels_count = 0
vowels={"a","e","i","o","u"}
for i in v:
    if i in vowels:
        vowels_count += 1  #?
print(f"The number of vowels in the string is: {vowels_count}")
print("completed")


# Write a program to calculate the average of all elements in a list using a for loop.
l=[1,2,3,4,5,6,7,8,9,10]
total=0
for i in l:
    total += i    #?
average = total / len(l)
print(f"The average of the elements in the list is:{average}") #?
print("completed")


# Write a program to print the following pattern using a for loop:
# *
# **
# ***
# ****
# *****
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()


# Write a program to print the square of each number from 1 to 10 using a for loop.
for i in range(1,11):
    i=i*i
    print(i)

# Write a program to print each character of a string using a for loop.
s="Python"
for i in s:
    print(i)

# Write a program to calculate the sum of all elements in a list using a for loop.
l=[1, 2, 3, 4, 5]
sum=0
for i in l:
    sum=sum+i
print(sum)

# Write a program to print elements at even indexes of a list using a for loop.
l=[10, 20, 30, 40, 50]
for i in range(0, len(l), 2):
    print(l[i])

# Write a program to print all odd numbers from 1 to 20 using a for loop.
for i in range(1,21,2):
    print(i)





