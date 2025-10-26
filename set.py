myset ={"apple","banana","cherry"}
myset.add("orange")
print(myset)
# Another way to add multiple elements to a set using update() method
theset ={"apple", "banana", "cherry"}
theset.update(["orange","mango","grapes"])
print(theset)
 
theset.remove("banana")
print(theset)

# Accessing set items
for x in theset:
    print(x)

# Checking if an item exsits in a set
print("banana" in theset)
print("orange" in theset)
print("apple"in theset)