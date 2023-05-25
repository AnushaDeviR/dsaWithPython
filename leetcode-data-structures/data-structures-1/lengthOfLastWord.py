'''
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 
'''

def lengthOfLastWord(self, s: str) -> int:

    '''
    # brute-force:
    words = s.split() 
    return len(words[-1])
    '''

    sLen = 0 
    lastIndex = len(s) - 1

    while s[lastIndex] == " ": 
        lastIndex -= 1
    while lastIndex >= 0 and s[lastIndex] != " ": 
        sLen += 1
        lastIndex -= 1
    return sLen

