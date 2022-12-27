'''
Pairs
Write a function to find all pairs of an integer array whose sum is equal to a given number.

Example

pairSum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
Output : ['2+5', '4+3', '3+4', '-2+9']
'''
myList = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]


def pairSum(arr, n):
    sumArray = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if (arr[i] + arr[j]) == n:
                sumArray.append(str(arr[i]) + "+" + str(arr[j]))
    return sumArray


print(pairSum(myList, 7))
