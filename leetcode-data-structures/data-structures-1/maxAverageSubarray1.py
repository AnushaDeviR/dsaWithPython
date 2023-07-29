'''
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous sub-array whose length is equal to k that has the maximum average value and return this value. 
Any answer with a calculation error less than 10-5 will be accepted.

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
Input: nums = [5], k = 1
Output: 5.00000
 
Constraints:
n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104
'''

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        curr_avg, window_sum = 0, 0

        for i in range(k):
            '''
            loop within the range of k (size of the sliding window) to get the current average value of the initial window 
            '''
            window_sum += nums[i]
        curr_avg = window_sum/k

        for i in range(k, len(nums)):
            '''
            Within the range of k, len(nums) -> the window sum is calculated for the remaining windows sliding with the size of k.
            While sliding to the next window, its left most value is left out which needs to be opted out when calculating for the 
            window_sum (hence the nums[i-k] is used to subtract it from the current window). 
            So window_sum = current_window - left out values from old_window. 
            Once the window_sum has been determined: 
            the max average value can be calculated by comparing the current average values from the windows and 
            the initial average value.
            '''
            print(nums[i-k]) # the values that needs to be left out to calculate the sum of the remaining windows
            window_sum += nums[i] - nums[i-k]
            curr_avg = max(curr_avg, window_sum/k)

        return float(curr_avg)
