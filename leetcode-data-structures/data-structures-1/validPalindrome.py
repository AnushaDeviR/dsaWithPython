'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
'''


def isPalindrome(self, s: str) -> bool:
    # convert to lowercase

    s_lower = s.lower()

    # remove all non-alphanumeric characters
    s_raw = [i for i in s_lower if i.isalnum()]

    # edge case => if s is empty then return true
    if s_raw == " " or len(s_raw) == 1:
        return True

    # use two-pointers to check if each letters match by placing one pointer at the left and right

    l = 0
    r = len(s_raw) - 1

    while l <= r:
        if s_raw[l] != s_raw[r]:
            return False

        l += 1
        r -= 1
    return True

    
    
    
    
