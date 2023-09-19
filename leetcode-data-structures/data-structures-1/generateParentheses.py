'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints: 1 <= n <= 8
'''

from typing import List

def generateParenthesis(self, n: int) -> List[str]:
    stack = []
    res = []

    # create a recursion (backtracking fn.) to add open brackets and closing brackets

    def backtrack(open, close):
        # base case: if open == close == n

        if open == close == n:
            res.append("".join(stack))
            return

        if open < n:
            stack.append("(")
            backtrack(open+1, close)
            stack.pop()

        if close < open:
            stack.append(")")
            backtrack(open, close+1)
            stack.pop()

    backtrack(0, 0)
    return res
