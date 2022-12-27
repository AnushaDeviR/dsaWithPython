'''
2D Lists
Given 2D list calculate the sum of diagonal elements.

Example

myList2D= [[1,2,3],[4,5,6],[7,8,9]] 
 
sumDiagonal(myList2D) # o/p => 15

'''
myList2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def sumDiagonal(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i][i]
    return sum


print(sumDiagonal(myList2D))
