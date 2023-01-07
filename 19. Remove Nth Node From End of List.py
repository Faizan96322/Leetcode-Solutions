# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head.next:
            return None
        front=head
        back = head
        counter = 0
        flag = False
        while counter<=n:
            if(not front):
                flag = True
                break
            front = front.next
            counter+=1
        while front:
            front = front.next
            back = back.next
        if not flag:
            temp = back.next
            back.next = temp.next
            temp.next = None
        else:
            head = head.next
        return head
