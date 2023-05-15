'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''


def longestCommonPrefix(self, strs: List[str]) -> str:

    temp = ''

    # loops through the indices of strs[0]
    for i in range(len(strs[0])):
        # loops through each characters of the corresponding strings
        for chars in strs:
            '''
            if each character is not equal to the characters of the 
            string on index-0:
            then return empty string (temp)
            else concat strs[0][i] into temp

            ''' 
            if len(chars) == i or chars[i] != strs[0][i]:

                return temp
        temp += strs[0][i]

    return temp
