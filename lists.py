mylist=["apple","banana","cherry"]
print(mylist)
# print(type(mylist))
# print(len(mylist))
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[-1])
# print(mylist[-2])
# print(mylist[-3])
# print(mylist[1:])
# print(mylist[1:3])
# print(mylist[:2])
# print(mylist[1:3])

# change items in list
# mylist[1]="orange"
# print(mylist)
# # change range of items in list
# mylist[1:3]=["orange","kiwi"]
# print(mylist)
# # add items to list
# mylist.append("orange")
# print(mylist)
# # add items to list at specific index
# mylist.insert(1,"orange")
# print(mylist)
# # remove items from list
# mylist.remove("orange")
# print(mylist)
# mylist.pop(1)
# print(mylist)
# mylist.pop()
# print(mylist)
# del mylist[1]
# print(mylist)
# mylist.clear()
# print(mylist)
# loop through list
# for x in mylist:
#     print(x)
# for i in range(len(mylist)):
#     print(mylist[i]) 
# Sort list
# mylist.sort()
# print(mylist)
# # Sort list in reverse order
# mylist.sort(reverse=True)
# print(mylist)
# mylist.reverse()
# print(mylist)
# # Copy list
# mylist2=mylist.copy()
# print(mylist2) 
# Join list
numlist=[1,2,3]
# newlist=mylist+numlist
# print(newlist)
# mylist.extend(numlist)
# print(mylist)
for i in range(len(numlist)):
    mylist.append(numlist[i])
print(mylist)  