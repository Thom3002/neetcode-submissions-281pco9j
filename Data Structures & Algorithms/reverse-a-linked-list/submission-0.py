# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

        # 1 -> 2 -> 3 -> null
        #prev = null
        # curr curr.next curr.next.next
        #curr.next = prev    
        # 1 -> null
        # nxt = curr.next 
        # curr = nxt
        # prev = curr