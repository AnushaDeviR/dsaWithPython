'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

'''


def isAnagram(self, s: str, t: str) -> bool:
    
    '''
    1. create a hashmap for s and t and store those letters as key, count as a property
    2. iterate through it and increment the count in hashmap
    3. if all counts of the stored letters in s are equal to t then retun true
    '''
    if len(s) != len(t): 
        return False

    count_s, count_t = {}, {}
    
    for letters in s: 
        if letters in count_s: 
            count_s[letters] += 1
        else: 
            count_s[letters] = 1

    for letters in t: 
        if letters in count_t: 
            count_t[letters] += 1
        else: 
            count_t[letters] = 1

    return count_s == count_t


    # '''
    # using get() in hashmap
    # ref: https://www.youtube.com/watch?v=9UtInBqnCgA&ab_channel=NeetCode
    # '''

    # if len(s) != len(t): 
    #     return False

    # count_s, count_t = {}, {} 

    # for letter in range(len(s)): 
    #     count_s[s[letter]] = 1+ count_s.get(s[letter], 0)
    #     count_t[t[letter]] = 1+ count_t.get(t[letter], 0)

    # return count_s == count_t
        

        
