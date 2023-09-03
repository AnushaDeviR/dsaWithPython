'''
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
'''
                
def containsDuplicate(self, nums: List[int]) -> bool:
    '''
    The below brute-force code takes time complexity of O(n^2) and space complexity of O(1)
    '''

    # count = 0
    # for i in range(0, len(nums)):
    #     for j in range(i+1, len(nums)):
    #         if nums[i] == nums[j]:
    #             print(nums[j])
    #             return True
    
    '''
    set() function returns randomized unordered unique (no elements) 
    elements from the list
    '''
    numSet = set(nums) 
    return True if len(nums) != len(numSet) else False
