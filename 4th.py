""" Exercise 4: Write a method to print first name and last name from full name.

Example:
Input: Arafat Rahman Sunny
Output: First name: Arafat, Last name: Sunny"""

def printFirstLastName(fullname):
    
    names = fullname.strip().split()

    print("First Name:",names[0])
    print("Last name:",names[-1])

printFirstLastName("Mohsin ibna hossain Mahmud")