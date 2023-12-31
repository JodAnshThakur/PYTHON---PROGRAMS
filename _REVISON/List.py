# Lists are mutable

l1 = [45,16,148,1194,"Ansh Thakur", "TopG"]
l2 = [5,6,148,45]

# print()
# print(l1+l2) #For concating two or more list in one list

print(l1.index(16))

slicing = l1[0:5] 
print(slicing)

# l1.append("WhereIam") #Adds the element in the last index
# print(l1)

# l1.insert(1,"ImHere")
# print(l1)

# l2.sort()
# print(l2)

# l1.remove(45) #Remove Element
# print(l1)

# l2.pop(3)
# print(l2) #After sorting l2 element 148  is at the last index

# del l1[0]
# print(l1)

# print(sum(l2)) #56 as 148 is already poped