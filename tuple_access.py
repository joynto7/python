newTuple = ("apple","banana","cherry","Orange","kiwi")
# Accessing elements in a tuple using positiv and negative  indexing and slicing
print(newTuple[0])
print(newTuple[2])
print(newTuple[-1])

# Accessing a range of emelents in a tuple using rangs of index
print(newTuple[1:4])
print(newTuple[:4])

# Using in keyword to check if an element exists in the tuple
if "apple" in newTuple:
    print("Yes")
else:
    print("No")    


    