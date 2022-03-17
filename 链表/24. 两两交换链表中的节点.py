# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 迭代法 很好用
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        # 哑结点 用于最后返回结果
        dummy = ListNode()
        dummy.next = head

        # 用两个指针反转
        pre, cur = dummy, head

        while cur and cur.next:
            # 保存 cur
            tmp = cur
            # 后移
            cur = cur.next
            # tmp指向cur的下一个
            tmp.next = cur.next
            # cur指向tmp
            cur.next = tmp
            # pre 指向 cur
            pre.next = cur
            pre = pre.next.next
            cur = cur.next.next
        return dummy.next