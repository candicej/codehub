# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 思想：https://leetcode-cn.com/problems/reverse-linked-list-ii/solution/java-shuang-zhi-zhen-tou-cha-fa-by-mu-yi-cheng-zho/
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        # 将 pre 移动到第一个要反转的节点的前面，将 cur 移动到第一个要反转的节点的位置上
        pre = dummy
        for i in range(1, left):
            pre = pre.next
        cur = pre.next

        for j in range(0, right - left):
            # 获取需要插入的节点
            next_node = cur.next
            # 更改cur节点的下一个节点
            cur.next = cur.next.next

            # 关键就在这里！！！！！！！注意！！！！！
            # 这里不能等于 cur, 因为cur的值始终不变！ 要让next_code.next 是pre节点的下一个节点 貒插入
            next_node.next = pre.next
            # pre指向
            pre.next = next_node

        return dummy.next




