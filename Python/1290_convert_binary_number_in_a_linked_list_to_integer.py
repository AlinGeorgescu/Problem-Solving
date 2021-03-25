#!/usr/bin/env python3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        acc = head.val
        head = head.next

        while head != None:
            print(acc)
            acc = acc << 1 | head.val
            head = head.next

        return acc
