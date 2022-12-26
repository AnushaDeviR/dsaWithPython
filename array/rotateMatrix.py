import numpy as np
# rotation of matrix (NxN matrix)
'''
pseudocode: 
for i = 0 to n:
    temp = top[i]
    top[i] = left[i]
    left[i] = bottom[i]
    bottom[i] = right[i]
    right[i] = temp
'''

myArray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print('original matrix:')
print(myArray)


def rotateMatrix(array):
    n = len(array)
    # n//2 -> returns the number of layers in a matrix
    # iterate through each row in the matrix
    for layer in range(n//2):
        # first row
        first = layer
    # last row
        last = n - layer - 1
        print(layer)
    # iterates through each column in the matrix
        for i in range(first, last):
            top = array[layer][i]  
            # move left element to top position
            array[layer][i] = array[-i-1][layer]
            # move bottom element to left position
            array[-i-1][layer] = array[-layer-1][-i-1]
            # move right element to bottom position
            array[-layer-1][-i-1] = array[i][-layer-1]
            # move top element to right position
            array[i][-layer-1] = top
    return myArray


print('rotated matrix: ')
print(rotateMatrix(myArray))
