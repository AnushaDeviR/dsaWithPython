'''
Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, then return its index. 
Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
'''

def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    l =0
    r = len(nums) - 1
    
    while l <= r:
        midValue = (l+r) // 2

        if nums[midValue] < target: 
            l = midValue + 1
        elif nums[midValue] > target: 
            r = midValue - 1
        else: 
            return midValue
    return -1

# test

nums = [-1,0,3,5,9,12]
print(search(nums, 9))