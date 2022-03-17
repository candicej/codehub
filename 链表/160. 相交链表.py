# 方法一 创建hash表
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        res = set()
        while headA:
            res.add(headA)
            headA = headA.next
        while headB:
            if headB in res:
                return headB
            headB = headB.next
        return None

# 方法二 进阶，不使用额外空间
# 方法 利用两个链表的长度关系
# https://leetcode-cn.com/problems/intersection-of-two-linked-lists/solution/intersection-of-two-linked-lists-shuang-zhi-zhen-l/
# 设「第一个公共节点」为 node ，「链表 headA」的节点数量为 aa ，「链表 headB」的节点数量为 bb ，「两链表的公共尾部」的节点数量为 cc ，则有：
# 头节点 headA 到 node 前，共有 a - c 个节点；
# 头节点 headB 到 node 前，共有 b - c 个节点；
# 所以走完A再走B 就相等了
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A = headA
        B = headB
        # 不管相不相交，都会相等，不会造成死循环
        while A!= B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A