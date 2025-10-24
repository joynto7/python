#converting tuple to list and add a new element using append() method
oldTuple = ("apple","banana","cherry")
# Convert tuple to list 
newList = list(oldTuple)
#Add a new element to the list 
newList.append("orange")
print(newList)
# convert the list back to tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)