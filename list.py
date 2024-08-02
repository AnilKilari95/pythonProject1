#Create a list called numbers with integers from 1 to 10. Perform the following operations:
numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers)
#Add the number 11 to the end of the list.
numbers.append(11)
print(numbers)
#Remove the number 5 from the list.
numbers.remove(5)
print(numbers)
#Find and print the index of the number 7.
index_seven = numbers.index(7)
print(index_seven)
#Replace the number 8 with 88.
numbers[6] = 88
print(numbers)
#Print the final list.
print(numbers)

#1. Changing Elements in a List
'''Given a list fruits = ["apple", "banana", "cherry"],
change the second item from "banana" to "blueberry".
Expected Output:
# Output: ['apple', 'blueberry', 'cherry']'''
fruits = ['apple', 'banana', 'cherry']
fruits[1]= 'blueberry'
print(fruits)

#Adding an Element to the End of the List
'''Start with the list numbers = [1, 2, 3, 4, 5]. Add the number 6 to the end of the list.
Expected Output:
# Output: [1, 2, 3, 4, 5, 6]'''
numbers = [1,2,3,4,5]
numbers.append(6)
print(numbers)

#Removing an Element from a List
'''Question: Given the list colors = ["red", "green", "blue", "yellow"],
remove the color "green" from the list.
# Output: ['red', 'blue', 'yellow']'''
colors = ['red', 'green', 'blue', 'yellow']
colors.remove('green')
print(colors)

# Inserting an Element at a Specific Position
''''Given the list animals = ["cat", "dog", "rabbit"],
insert the element "hamster" at index 1.
Output: ['cat', 'hamster', 'dog', 'rabbit']'''
animals = ['cat', 'dog', 'rabbit']
animals.insert(1,'hamster')
print(animals)


# Extending a List with Another List
'''Start with the list list1 = [1, 2, 3] and 
extend it with another list list2 = [4, 5, 6].'''
#Output: [1, 2, 3, 4, 5, 6]
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)

# Popping an Element from a List
'''Given the list items = [10, 20, 30, 40, 50], 
use the pop() method to remove and return the last element.'''
# Output: 50
# items after pop: [10, 20, 30, 40]
list_items = [10, 20, 30, 40, 50]
list_items.pop()
list_items.pop(1)
print(list_items)

#Deleting an Element by Index
'''Given the list cities = ["New York", "Los Angeles", "Chicago", "Houston"], 
delete the element at index 2.'''
# Output: ['New York', 'Los Angeles', 'Houston']
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston']
del cities[2]
print(cities)

#Deleting a Slice of Elements
'''Given the list numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9], 
delete the elements from index 2 to 5.'''
# Output: [1, 2, 6, 7, 8, 9]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del numbers[2:5]
print(numbers)

#Clearing All Elements from a List
'''Start with the list letters = ['a', 'b', 'c', 'd'] and 
use the clear() method to remove all elements.'''
# Output: []
letters = ['a', 'b', 'c', 'd']
letters.clear()
print(letters)

#Finding and Removing an Element
'''Given the list scores = [85, 90, 95, 100], find the score 95 and remove it from the list.'''
# Output: [85, 90, 100]
scores = [85, 90, 95, 100]
scores.remove(95)
print(scores)

#ascending order
l = [10, 2, 30, 1, 40]
l.sort()
print(l)

# descending order
l = [1, 30, 5, 4]
l.sort(reverse = True)
print(l)

# copy a list
l = [1, 2, 3, 4]
m = l.copy()
print(m)

# reverse a list
l = [1, 2, 3, 4,5]
l.reverse()
print(l)

# remove extra same items in list
l =['hello', 'world', 'hello', 'word']
for i in l:
    l.remove('hello')
    print(l)

# nested list
l = [[1, 2], 10, 20, [10, 30]]
print(l[0])
print(l[0][0])
print(l[3][1])


# Tuple
t = ('a', 'b', 'c', 'd')
print(t[0::2])
print(t[0::3])
print(t[0::4])
print(t[-4:-2])

t = (10, 20, 30, 40, 50)
y = list(t)
y[1] = 200
t = tuple(y)
print(t)

t = ('apple', 'banana', 'cherry', 'grapes')
a, *b, c = t
print(a)
print(b)
print(c)

# count()
t = ('apple', 'banana', 'cherry', 'apple')
print(t.count('apple'))

#t =('apple', 'banana', 'cherry')
#print(t.index['cherry'])

#Creating a Tuple
#Question: Create a tuple named fruits that contains
# three elements: "apple", "banana", and "cherry". Print the tuple.
# Output: ('apple', 'banana', 'cherry')
t1 = ('apple', 'banana', 'cherry')
print(t1)


#2. Accessing Elements in a Tuple
#Question: Given the tuple numbers = (10, 20, 30, 40, 50), access and print the third element.
# Output: 30
numbers = (10, 20, 30, 40, 50)
print(numbers[2])


#3. Slicing a Tuple
#Question: Given the tuple colors = ('red', 'green', 'blue', 'yellow'),
# slice and print the elements from index 1 to 3.
# Output: ('green', 'blue', 'yellow')
colors = ('red', 'green', 'blue', 'yellow')
print(colors[1:])

#4. Concatenating Tuples
#Question: Create two tuples: tuple1 = (1, 2, 3) and tuple2 = (4, 5, 6). Concatenate them and print the result.
# Output: (1, 2, 3, 4, 5, 6)
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = tuple1 + tuple2
print(tuple3)


#5. Repeating Elements in a Tuple
#Question: Given the tuple repeat = ('a', 'b'), repeat it three times and print the result.
# Output: ('a', 'b', 'a', 'b', 'a', 'b')
repeat = ('a', 'b')
t = repeat * 3
print(t)

#6. Checking Membership in a Tuple
#Question: Given the tuple numbers = (5, 10, 15, 20),
# check if the number 15 is in the tuple and print the result (True or False).
# Output: True
numbers = (5, 10, 15, 20)
x = 15
y = x in numbers
print(y)


#7. Counting Occurrences of an Element
#Question: Given the tuple letters = ('a', 'b', 'c', 'a', 'b', 'a'),
# count and print the number of occurrences of the letter 'a'.
# Output: 3
letters = ('a', 'b', 'c', 'a', 'b', 'a')
print(letters.count('a'))



#8. Finding the Index of an Element
#Question: Given the tuple values = (1, 2, 3, 4, 5), find and print the index of the value 4.
# Output: 3
values = (1, 2, 3, 4, 5)
print(values.index(4))

#9. Unpacking a Tuple
#Question: Given the tuple person = ('John', 25, 'Engineer'),
# unpack it into three variables name, age, and occupation, and print these variables.
# Output:
# Name: John
# Age: 25
# Occupation: Engineer
person = ('John', 25, 'Engineer')
Name, Age, Occupation = person
print("Name:", Name)
print("Age:", Age)
print("Occupation:", Occupation)



#10. Swapping Values Using Tuples
#Question: Swap the values of two variables a and b using a tuple.
# For example, if a = 10 and b = 20, after swapping, a should be 20 and b should be 10.
# After swapping:
# a: 20
# b: 10
a, b = (10, 20)
a = b
b = a - 10
print('a:', a)
print('b:', b)
