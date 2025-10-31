a = 10 
b = 23

if a > b:
    print("a is greate than b")
else:
    print("b is greater than a")

# multiple statements in if block
age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")

# elif statement
marks = 65
if marks >= 80:
   print("Grade A+")
elif marks < 80 and marks >=70:
   print("Grade A")

#nested if statement 
score = 85
if score >= 50:
   print("You passed the exam")
elif score >= 75:
   print("You passed with good marks")
elif score >= 90:
   print("You passed with excellent marks")
elif score < 50 :
   print("Ypu failed the exam")
else:
   print("invalid Score")