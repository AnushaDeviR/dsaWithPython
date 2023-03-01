'''
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:
Input: s = "God Ding"
Output: "doG gniD"
'''

def reverseWords(self, s: str) -> str:
        
    l = 0 
    res = s[::-1].split(' ')
    r = len(res) - 1

    while l <= r:
        res[l], res[r] = res[r], res[l]
        l += 1
        r -= 1
    return ' '.join(res)