'''
Write a function to find the duplicate number on given integer array/list.

Example

removeDuplicates([1, 1, 2, 2, 3, 4, 5])
Output : [1, 2, 3, 4, 5]
'''

myList = [1, 1, 2, 2, 3, 4, 5]


def removeDuplicates(arr):
    newArray = []
    for i in arr:
        if i not in newArray:
            newArray.append(i)
    print(newArray)


print(removeDuplicates(myList))
