'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
'''
def moveZeroes(self, nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """

# Pointer L starts off at index 0 and pointer R iterates throughout the array
    l = 0 
    for r in range(len(nums)):
        # if there is a non-zero number on the index of R, then the numbers on the pointers are swapped and pointer L is moved forward
        if nums[r]:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1

    return nums