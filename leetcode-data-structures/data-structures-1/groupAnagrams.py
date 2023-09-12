from collections import defaultdict

'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
'''

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

    # 1. create a hashmap that can store lists where the default value is a list
    result = defaultdict(list)

    # 2. For each words in strs the letters are counted
    for words in strs:
        count = [0] * 26
        for c in words:
            # 3. map the letters (a-z) with numbers (0-25) to increment count whenever it encounters a letter
            # ord() -> returns an integer representing the Unicode character; ord("a") = 97
            count[ord(c) - ord("a")] += 1
        # 4. Append the grouped anagrams according to the count pattern of each words
        result[tuple(count)].append(words)
    print(result)
    return result.values()
