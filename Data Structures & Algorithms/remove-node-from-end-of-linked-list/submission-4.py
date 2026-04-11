# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        i = count - n
        if i < 0 or count == 1:
            return None
        
        curr = head
        count = 0
        prev = None
        while curr:
            if count == i:
                if prev:
                    prev.next = curr.next
                else:
                    head = curr.next
                return head 
            prev = curr
            curr = curr.next
            count += 1
        
        return head 
