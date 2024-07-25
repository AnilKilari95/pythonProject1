def first_last_same(numberlist):
    print("given list:",numberlist)
    first_num = numberlist[0]
    last_num = numberlist[-1]
    if first_num == last_num:
        return True
    else:
        return False
numbers_x = [10, 20, 30, 40, 10]
print("result is", first_last_same(numbers_x))

numbers_y = [75, 65, 35, 75, 30]
print("result is", first_last_same(numbers_y))


i=0
while i<3:
    print(i)
    i+=1
else:
    print(0)

print([[i+j for i in "abc"] for j in "def"])

i=0
while i<5:
    print(i)
    i+=1
    if i==3:
        break
else:
    print(0)

i=1
while True:
    if i%3==0:
        break
    print(i)
    i+=1

i = 1
while i < 6:
  print(i)
  i += 1

#no=int(input("enter any number"))
#print("You entered:",no,sep='')

#no=float(input("enter float number"))
#print("Value of Pi:",no,sep="")

#no=input("enter numbers")
#x,y,z=no.split(" ")
#sum=int(x)+int(y)+int(z)
#print("Sum of inputs:",sum,sep="")

l=[1,2,3,4,5,5]
print(l)
l.insert(5,6)
print(l)
l.append(7)
print(l)
l.remove(7)
print(l)
d={"a":1,"b":2}
print(d)
print(d.values())
d["c"]=3
print(d)

s={1,2,3,4,5}
s.add(6)
print(s)
s.remove(6)
print(s)

l="hello"
print(l[2:])

l=[1,2,3,4,5]
l1=[6,7,8,9,10]
l3=l+l1
print(l3)


for i in range(1,11):
    i=i+1
    print(i)
result = [i+1 for i in range(1, 11)]
print(result)

l=[1,5,7,3,8,4,2]
l.sort()
print(l)

d={"a":1,"b":2,"c":3}
print(d)
for i,j in d.items():
    print(i,j)



d={"a":1,"b":2,"c":3}
x=d.get("a")
print(x)

#shallow copy
import copy

original_list = [1, 2, [3, 4]]
shallow_copied_list = copy.copy(original_list)

# Modifying an element in the nested list
shallow_copied_list[2][0] = 'changed'

print("Original list:", original_list)  # Output: [1, 2, ['changed', 4]]
print("Shallow copied list:", shallow_copied_list)  # Output: [1, 2, ['changed', 4]]

#deep copy
import copy

original_list = [1, 2, [3, 4]]
deep_copied_list = copy.deepcopy(original_list)

# Modifying an element in the nested list
deep_copied_list[2][0] = 'changed'

print("Original list:", original_list)  # Output: [1, 2, [3, 4]]
print("Deep copied list:", deep_copied_list)  # Output: [1, 2, ['changed', 4]]

l={"z":1,"x":2}
l1={"c":3,"v":4}
l.update(l1)
print(l)

l=[1,2,2,4,3,5,4,3,1]
l1=set(l)
print(l1)
l2=list(l1)
print(l2)

l=[1,2,3,4,5]
for i in range(5,0,-1):
    print(i)

#l=[10,20,30,40,50,60,70,80,90,100]
#for i in l:
 #   print(second highest number in i)

def second_largest(lst):
    # Remove duplicates by converting the list to a set, then back to a list
    unique_lst = list(set(lst))

    # Check if there are at least two unique numbers
    if len(unique_lst) < 2:
        return None  # or raise an exception

    # Sort the list in descending order
    unique_lst.sort(reverse=True)

    # Return the second element
    return unique_lst[1]


# Example usage
my_list = [10, 20, 4, 45, 99, 99]
result = second_largest(my_list)
print(result)  # Output: 45


def is_palindrome(s):
    # Normalize the string by converting it to lowercase and removing non-alphanumeric characters
    s = ''.join(char.lower() for char in s if char.isalnum())

    # Check if the string equals its reverse
    return s == s[::-1]


# Example usage
test_string = "A man, a plan, a canal, Panama"
result = is_palindrome(test_string)
print(result)  # Output: True

def remove_nth_from_end(head, n):
    # Create a dummy node to simplify edge cases, e.g., removing the head
    dummy = ListNode(0)
    dummy.next = head
    first = dummy
    second = dummy

    # Move first pointer to the n+1-th node from the beginning
    for _ in range(n + 1):
        if first is None:
            return head  # If n is larger than the length of the list
        first = first.next

    # Move both pointers until first reaches the end
    while first is not None:
        first = first.next
        second = second.next

    # Remove the nth node from the end
    second.next = second.next.next

    return dummy.next



# Helper function to print the linked list
def print_list(head):
    while head:
        print(head.value, end=" -> ")
        head = head.next
    print("None")

# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# Remove the 2nd node from the end (which is node with value 4)
new_head = remove_nth_from_end(head, 2)

# Print the updated linked list
print_list(new_head)  # Output: 1 -> 2 -> 3 -> 5 -> None


#Write a Python function to merge two sorted lists into one sorted list.
def merge_sorted_lists(list1, list2):
    merged_list = []
    i, j = 0, 0

    # Traverse both lists and append the smaller element to the merged list
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # If there are remaining elements in list1, append them
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    # If there are remaining elements in list2, append them
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list

def merge_sorted_lists(list1, list2):
    return sorted(list1 + list2)

#Write a Python function to find the longest common prefix among a list of strings.
