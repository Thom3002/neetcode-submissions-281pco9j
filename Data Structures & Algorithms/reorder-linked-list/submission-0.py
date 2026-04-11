# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second = slow.next
        slow.next = None
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        # first => 0 -> 1 -> 2 -> 3 -> null
        # prev => 6 -> 5 -> 4 -> null
        second = prev # 6 
        first = head # 0
        # 
        # tmp1 = 1
        # tmp2 = 5
        # 
        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second 
            second.next = tmp1

            first = tmp1
            second = tmp2
            # 0 -> 6 -> 1


            
