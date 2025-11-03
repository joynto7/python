filename = input("Enter filename: ")
with open(filename, 'r') as file:
    text = file.read()
words = text.split()
print(f"Total words: {len(words)}")
