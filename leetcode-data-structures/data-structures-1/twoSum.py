'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

 
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
'''

def twoSum(self, nums: List[int], target: int) -> List[int]:

    prevMap = {} #hash map-> {value:index}

    for i, n in enumerate(nums): #enumerate() acts as a counter for nums
    # find difference of target and nums i.e. n
        difference = target - n
        # return value and index of the difference
        if difference in prevMap: 
            return [prevMap[difference], i]
        prevMap[n] = i
    return 
