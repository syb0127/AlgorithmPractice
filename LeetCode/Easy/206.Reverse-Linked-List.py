# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        pointer = None
        while (head != None):
            curr = head
            head = head.next
            curr.next = pointer
            pointer = curr
        return pointer
    
        """
        :type head: ListNode
        :rtype: ListNode
        """
        