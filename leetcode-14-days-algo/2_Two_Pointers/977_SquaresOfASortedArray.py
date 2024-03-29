'''
Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
'''

def sortedSquares(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    result = [] 

    l = 0 
    r = len(nums) - 1
    while l <= r: 
        sqr_l = nums[l] * nums[l]
        sqr_r = nums[r] * nums[r] 
        if sqr_l > sqr_r: 
            result.append(sqr_l)
            l += 1
        else: 
            result.append(sqr_r)
            r -= 1
        
    return result[::-1]
