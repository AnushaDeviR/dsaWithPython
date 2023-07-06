'''
You are given a string `s`. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be `s`.

Return *a list of integers representing the size of these parts*.

**Example 1:**

```
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

```

**Example 2:**

```
Input: s = "eccbbbbdec"
Output: [10]

```

**Constraints:**

- `1 <= s.length <= 500`
- `s` consists of lowercase English letters.
'''


def partitionLabels(self, s: str) -> List[int]:

    lastOccurance = {}
    out = []

    l, r = 0, 0

    for count, value in enumerate(s):
        # inserts the index of the last occured letter
        lastOccurance[value] = count

    for count, value in enumerate(s):
        l += 1
        # gets the max. index from enumerated value
        r = max(r, lastOccurance[value])

        if r == count:
            out.append(l)
            l = 0

    return out
