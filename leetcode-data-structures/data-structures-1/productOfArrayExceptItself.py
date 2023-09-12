'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 
Follow up: Can you solve the problem in O(1) extra space complexity? 
(The output array does not count as extra space for space complexity analysis.)
'''


def productExceptSelf(self, nums: List[int]) -> List[int]:
    
    # initialize result with 1 for the length of nums 
    result = [1] * len(nums)

    prefix = 1
    postfix = 1

    # loops from left to right of nums
    for i in range(len(nums)): 
        result[i] = prefix
        # product of numbers from the current position and its values on the left
        prefix *= nums[i]

    # loops from right to left of nums
    for i in range(len(nums)-1, -1, -1): 
        # keep the values of prefix in result and update upon postfix calculations
        result[i] *= postfix
        # product of prefix values to the remaining positions on the right
        postfix *= nums[i]
    return result
