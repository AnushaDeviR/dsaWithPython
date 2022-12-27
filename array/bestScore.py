'''
Best Score
Given a list, write a function to get first, second best scores from the list.

List may contain duplicates.

Example

myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
firstSecond(myList) # 90 87
'''

myList = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]


def firstSecond(arr):
    newArray = arr.copy()
    max1 = max(newArray)
    max1Index = newArray.index(max1)
    del newArray[max1Index]
    max2 = max(newArray)

    return max1, max2


print(firstSecond(myList))
