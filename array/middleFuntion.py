'''
Middle Function
Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

myList = [1, 2, 3, 4]
middle(myList)  # o/p: [2,3]
'''

myList = [1, 2, 3, 4, 0]


def middleFuntion(arr):
    newArray = arr.copy()
    del newArray[0]
    del newArray[-1]
    return newArray


print(middleFuntion(myList))
