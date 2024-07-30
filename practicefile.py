pv=0
for i in range(0,10):
    z=i+pv
    pv=i
    print("Current Number", i, "Previous Number ", pv, " Sum: ", z)



str="pynative"
for i in str[0::2]:
    print(i)



x="pynative"
print(x[4:])
print(x[2:])


numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
if numbers_x[0]==numbers_x[4]:
    print("result is True",numbers_x)
if numbers_y[0]==numbers_y[4]:
    print("result is True",numbers_y)
else:
    print("result is False")

num_list=[10,20,33,46,55]
print("given list is",num_list)
print("divisible by 5")
for i in num_list:
    if i%5==0:
        print(i)

str_x = "Emma is good developer. Emma is a writer"
cnt=str_x.count("Emma")
print(cnt)

str_x = "Emma is a good developer. Emma is a writer"
substring = "Emma"

# Count the occurrences of the substring
count = str_x.count(substring)

# Print the result
print(f"{substring} appeared {count} times")




rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print(i, end=' ')
    print()

def is_palindrome(num):
    # Convert the number to a string
    str_num = str(num)
    # Check if the string is the same forwards and backwards
    return str_num == str_num[::-1]

# Test cases
numbers = [121, 125]

for number in numbers:
    if is_palindrome(number):
        print(f"Original number {number}\nYes. given number is palindrome number\n")
    else:
        print(f"Original number {number}\nNo. given number is not palindrome number\n")



