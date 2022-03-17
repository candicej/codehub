# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 参考https://leetcode-cn.com/problems/insertion-sort-list/solution/dui-lian-biao-jin-xing-cha-ru-pai-xu-by-leetcode-s/
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dummy = ListNode(-1)
        dummy.next = head

        # 链表的第一个节点 就是已经排好序的
        solved = head
        # 从链表的第二个元素开始插入
        cur = head.next
        while cur:
            # 如果大于，直接放在链表的尾巴上
            if solved.val <= cur.val:
                solved = solved.next

            else:
                # 需要从头开始遍历链表
                # 需要一个辅助指针
                pre = dummy
                # 如果小于等于就一直往后走
                while pre.next.val <= cur.val:
                    pre = pre.next
                # 挪一位
                solved.next = cur.next
                #  开始插入
                tmp = pre.next
                pre.next = cur
                cur.next = tmp
            # cur变回原来的位置
            cur = solved.next
        return dummy.next
