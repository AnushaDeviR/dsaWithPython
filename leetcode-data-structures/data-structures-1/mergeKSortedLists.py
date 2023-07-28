'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
 
Constraints:
k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists) == 0 or not lists:
            return None

        while len(lists) > 1:
            mergedList = []

            for k in range(0, len(lists), 2):
                list1 = lists[k]

                if (k+1) < len(lists):
                    list2 = lists[k+1]

                else:
                    list2 = None
            # perform merging of 2 sorted lists
                mergedList.append(self.merge2SortedLists(list1, list2))
            lists = mergedList
        return lists[0]

    def merge2SortedLists(self, l1, l2):
        temp = ListNode()
        result = temp

        while True:
            if l1 is None:
                result.next = l2
                break
            if l2 is None:
                result.next = l1
                break
            if l1.val <= l2.val:
                result.next = l1
                l1 = l1.next
            else:
                result.next = l2
                l2 = l2.next
            result = result.next
        return temp.next
