# Exercise 1: Take a number (0-100) from user and Use if statement to print corresponiding grade.
num = int(input("Enter a number (0-100):"))

if num>=90:
    print("A+")

elif num>=80:
    print("B+")

elif num>=70:
    print("C+")

elif num>=60:
    print("D+")

elif(num>=50):
    print("D")

else:
    print("F")