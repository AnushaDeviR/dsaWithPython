'''
Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]


Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
'''

from typing import List

def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    # 1.Initalize stacks, If no future day with higher temperature is found keep answer[i] == 0 instead.
    answer = [0] * len(temperatures)
    stack = []  # [[temp: index]]

    # 2. Loop through the input array and append stack with [temp: index]
    for i, temp in enumerate(temperatures):
        # 3. Loop until stack is not empty and temp is more than the previous temp => stack[-1][0] = last element of the sequence and the first value in the array which is temp
        while stack and temp > stack[-1][0]:
        
        #3.1. pop the stacked values with the loop condition and store the number of days it took to reach a higher temperature => i - stack_index
        stack_temp, stack_index = stack.pop()
        answer[stack_index] = i - stack_index
        print(answer)
        stack.append([temp, i])
    return answer
