mytuple=('apple', 'banana', 'cherry','orange', 'kiwi', 'melon', 'mango')  # Creating a tuple with multiple elements
print(mytuple)
mytuple[1]='aaa'
print(mytuple)
# mytuple[1] = 'orange'  # This will raise a TypeError because tuples are immutable
# print(mytuple[1])  # Accessing the second element of the tuple
# print(mytuple[0:2])  # Slicing the tuple to get the first two elements
# print(mytuple[-1])  # Accessing the last element of the tuple
# print(mytuple[1:])  # Slicing the tuple to get elements from index 1 to the end
# print(mytuple[:2])  # Slicing the tuple to get elements from the start to index 2
# print(mytuple[1:2])  # Slicing the tuple to get elements from index 1 to index 2 (exclusive)
# temp=list(mytuple)  # Converting tuple to list
# temp[1]='orange'  # Changing the second element of the list
# print(temp)  # Printing the modified list
# mytuple=tuple(temp)  # Converting list back to tuple
# (green,red,yellow) = mytuple  # Unpacking the tuple into variables
# print(green)  # Printing the first element of the tuple
# print(red)  # Printing the second element of the tuple
# print(yellow)  # Printing the third element of the tuple
# (green,*abcd)=mytuple  # Unpacking the tuple into variables, with *abcd capturing the rest
# print(green)  # Printing the first element of the tuple
# print(abcd)  # Printing the rest of the elements of the tuple
# (gree,*abcd,yellow)=mytuple
# print(*abcd)
# for i in range(len(mytuple)):
#     print(mytuple[i])  # Printing each element of the tuple using a for loop
