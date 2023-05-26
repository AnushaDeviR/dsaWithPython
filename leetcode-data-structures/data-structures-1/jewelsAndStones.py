'''
You're given strings jewels representing the types of stones that are jewels, 
and stones representing the stones you have. Each character in stones is a type of stone you have. 
You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

Example 2:
Input: jewels = "z", stones = "ZZ"
Output: 0

Constraints:
1 <= jewels.length, stones.length <= 50
jewels and stones consist of only English letters.
All the characters of jewels are unique.
'''

def numJewelsInStones(self, jewels: str, stones: str) -> int:

    stones_list = {} 
    isJewel = 0 

    for stone in stones: 
        if stone in stones_list: 
            stones_list[stone] += 1
        else:
            stones_list[stone] = 1
    print(stones_list)

    for j in range(len(jewels)): 
        if jewels[j] in stones_list:
            isJewel += stones_list[jewels[j]]

    return isJewel
