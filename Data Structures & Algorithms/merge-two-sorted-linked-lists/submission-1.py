# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val > list2.val:
            head = list2
            list2 = list2.next
        else:
            head = list1
            list1 = list1.next
        head.next = self.mergeTwoLists(list1,list2)
        return head
    # for production or something where your lists can become very large
    # it would be better to use an iterative approach with a dummy noade
    # so you don't recurse and allocate a bunch of memory.
        