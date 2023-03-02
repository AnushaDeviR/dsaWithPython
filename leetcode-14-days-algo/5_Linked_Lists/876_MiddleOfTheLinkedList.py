'''
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:
Linked List: [1] -> [2] -> [3] -> [4] -> [5]
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Linked List: [1] -> [2] -> [3] -> [4] -> [5] -> [6]
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

    temp = head
    # two - pointers: slow = slow + 1, fast = fast + 2 traversals
    slow = temp
    fast = temp 

# while fast pointer is not null; i.e. when fast pointer stays within the linked list 
    while fast and fast.next: 
        slow = slow.next
        fast = fast.next.next
    return slow