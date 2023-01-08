# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, headA, headB):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummyNode = ListNode(0)
  
        # Tail stores the last node
        tail = dummyNode
        while True:

            # If any of the list gets completely empty
            # directly join all the elements of the other list
            if headA is None:
                tail.next = headB
                break
            if headB is None:
                tail.next = headA
                break

            # Compare the data of the lists and whichever is smaller is
            # appended to the last of the merged list and the head is changed
            if headA.val <= headB.val:
                tail.next = headA
                headA = headA.next
            else:
                tail.next = headB
                headB = headB.next

            # Advance the tail
            tail = tail.next

        # Returns the head of the merged list
        return dummyNode.next
