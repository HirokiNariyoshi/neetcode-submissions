# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        target = target_node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                target.next = list1
                list1 = list1.next
            else:
                target.next = list2
                list2 = list2.next

            target = target.next
        # remainder is just whichever one is not none
        target.next = list1 or list2

        return target_node.next

        

