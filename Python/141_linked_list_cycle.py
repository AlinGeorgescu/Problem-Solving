# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next or not head.next.next:
            return False

        helper = head.next.next

        while helper.next and helper.next.next:
            if head.val == helper.val:
                return True

            helper = helper.next.next
            head = head.next

        return False
