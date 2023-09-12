'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.


Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
'''


def longestConsecutive(self, nums: List[int]) -> int:

    # get set of the input
    numSet = set(nums)
    print(numSet)
    # initialize sequence and a temp length (l) variable
    seq = 0
    l = 0
    # loop through the numSet
    for i in numSet:
        # check if the current integer is not the start of the consecutive sequence and set length to 1
        if i - 1 not in numSet:
            l = 1
            # while integer + length is in the numSet then increment the length
            while i + l in numSet:
                l += 1
        # get the max length of the consecutive sequence
        seq = max(l, seq)

    return seq
