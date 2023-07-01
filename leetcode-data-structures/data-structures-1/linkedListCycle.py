# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

            if (slow == fast):
                return True

        return False


''' 
Explanation: 
By using Floyd’s algorithm (cycle-finding algorithm) which uses 2 pointers - slow, fast method where slow starts at the 0th index and fast is at slow += 2. So when slow == fast then it means that there is a cycle. When a cycle exists in a LL no matter what slow and fast meets at a same node.
'''
