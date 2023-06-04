'''
Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.
Return any answer array that satisfies this condition.

Example 1:
Input: nums = [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

Example 2:
Input: nums = [2,3]
Output: [2,3]

Constraints:
2 <= nums.length <= 2 * 104
nums.length is even.
Half of the integers in nums are even.
0 <= nums[i] <= 1000
'''


def sortArrayByParityII(self, nums: list[int]) -> list[int]:

    o = 1  # tracks odd indices

    # iterates over even indices
    for i in range(0, len(nums), 2):
        # checks if the current even index is odd
        if nums[i] % 2:
            # continues searching for odd number
            while nums[o] % 2:
                # increments by 2 while going through the while loop
                o += 2
            # once an even number is found, it swaps to its correct index
            nums[i], nums[o] = nums[o], nums[i]

    return nums
