# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        # 找中间节点
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next

        # 翻转后面的链表
        pre = None
        cur = slow
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        # 比较
        while pre:
            if pre.val == head.val:
                pre = pre.next
                head = head.next
            else:
                return False

        return True



