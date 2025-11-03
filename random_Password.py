import random , string

length = int(input("Password Length:"))

chars = string.digits + string.ascii_letters + string.punctuation + string.ascii_uppercase +string.ascii_lowercase +string.digits

password = ''.join(random.choice(chars) for _ in range(length)) 
print("Generated Password:", password)
