# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        # head is first node
        while curr != None:
            temp = curr.next # store the next pointer in a temp

            curr.next = prev
            prev = curr
            curr = temp
        return prev
