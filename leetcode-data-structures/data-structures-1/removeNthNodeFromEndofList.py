'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
 
Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # inserts new dummy node previous to the head node
        dummy = ListNode(next=head)
        left = dummy
        right = head
        '''
        runs until n is not 0; by initializing n -= 1, 
        n becomes 0 at a point where it becomes the last increment for right, 
        hence this returns right being at a point where it is 2 pointers ahead of left (which is at head)
        '''

        while n > 0 and right:
            right = right.next
            n -= 1

        # runs until right is NONE; increment left and right by 1 node
        while right:
            left = left.next
            right = right.next

        print('Left pointer: ', left)
        # remove the next value of left which is `n`
        left.next = left.next.next

        return dummy.next
