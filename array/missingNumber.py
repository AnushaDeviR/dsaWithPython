'''
Missing Number
Write a function to find the missing number in a given integer array of 1 to 100.

Example

missingNumber([1, 2, 3, 4, 6], 6) # 5
'''

myList = [1, 2, 3, 4, 6]


def missingNumber(arr, totalCount):
    sumArray = sum(arr)
    actualSum = int(totalCount * ((totalCount + 1)/2))
    return actualSum - sumArray


print(missingNumber(myList, 6))
