'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Linked List = [1] -> [2] -> [3] -> [4] -> [5]
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]


Example 2:
Linked List = [1]
Input: head = [1], n = 1
Output: []

Example 3:
Linked List = [1] -> [2]
Input: head = [1,2], n = 1
Output: [1]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(next=head)
    previous = dummy
    current = head
    count = 0 

# finds the length of the linked list
    while current:
        count += 1
        current = current.next
    
# set current back to head to re-traverse
    current = head
    target = count - n 

    index = 0

    while current:
# checks if index of the corresponding node matches the target nth node
        if index == target:
            previous.next = current.next
            current = current.next
        else: 
            previous = previous.next
            current = current.next
        index += 1
# return head of the linked list
    return dummy.next
