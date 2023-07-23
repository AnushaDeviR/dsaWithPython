'''
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false

Constraints:
The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 
Follow up: Could you do it in O(n) time and O(1) space?
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        slow, fast = head, head

        # find middle node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print('middle:', slow)
        print('tail:', fast)

        # reverse the half after middle
        prev = None
        while slow:
            temp = slow.next
            prev = slow
            slow = temp

        print('prev: ', prev)

        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True

'''
    brute-force method: append the head.val into an array and use 2-pointers 
        arr = [] 

        while head: 
            arr.append(head.val)
            head = head.next

        print(arr)

        l, r = 0, len(arr) - 1

        while l < r: 
            if arr[l] != arr[r]: 
                return False
            l += 1
            r -= 1
        return True
'''
