'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
'''


def trap(self, height: List[int]) -> int:
    # 1. initialize variables: l, r, max_pointer values

    l, r = 0, len(height) - 1
    max_l, max_r = height[l], height[r]
    result = 0

    # 2. 2-pointers approach
    while l < r:
        # 2.1. shift pointer that has min height
        # 2.2. get max height of shifted pointer and current pointer height
        # 2.3. calculate: max_pointer - current pointer value

        if max_l < max_r:
            l += 1
            max_l = max(max_l, height[l])
            result += max_l - height[l]
        else:
            r -= 1
            max_r = max(max_r, height[r])
            result += max_r - height[r]

    return result
