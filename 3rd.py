"""Exercise 3: Define a method to add two lists and returns another list

Example:
Input: [3,4,5,1] and [6,7,2,8]
output: [9,11,7,9]"""

def addList(list1, list2):
    if len(list1) != len(list2):
        print("List lengths must be the same to add them.")
        return

    result = []
    for i in range(len(list1)):
        result.append(list1[i] + list2[i])
    
    return result

list1 = [10, 20, 30]
list2 = [40, 50, 60]

print(addList(list1, list2))
