# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 用归并排序
# https://leetcode-cn.com/problems/sort-list/solution/
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 对两个链表进行排序
        def merge(head1: ListNode, head2: ListNode) -> ListNode:
            dummyHead = ListNode()
            # 这里要设置两个新的头结点，不懂为什么不可以直接使用head1和head2
            temp, temp1, temp2 = dummyHead, head1, head2
            while temp1 and temp2:
                if temp1.val <= temp2.val:
                    temp.next = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp2
                    temp2 = temp2.next
                temp = temp.next
            if temp1:
                temp.next = temp1
            elif temp2:
                temp.next = temp2
            return dummyHead.next

        # 找到链表的中点，以中点为分界，将链表拆分成两个子链表。寻找链表的中点可以使用快慢指针的做法，快指针每次移动 22 步，慢指针每次移动 11 步，
        # 当快指针到达链表末尾 时,慢指针指向的链表节点即为链表的中点。
        def sortFunc(head: ListNode, tail: ListNode) -> ListNode:
            if not head:
                return head
            if head.next == tail:
                head.next = None
                return head
            slow = fast = head
            while fast != tail:
                slow = slow.next
                fast = fast.next
                if fast != tail:
                    fast = fast.next
            mid = slow
            return merge(sortFunc(head, mid), sortFunc(mid, tail))

        return sortFunc(head, None)
