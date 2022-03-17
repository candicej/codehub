#定义节点
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None
#将传入的数组转化为链表
def create_linked_list(arr):
    head = ListNode(arr[0])
    cur = head
    for i in range(1, len(arr)):
        cur.next = ListNode(arr[i])
        cur = cur.next
    return head
#传入链表头节点，以数组形式返回
def print_linked_list(head):
    cur = head
    res = []
    while cur:
        res.append(cur.val)
        cur = cur.next
    return res


class Solution():
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        # 将 pre 移动到第一个要反转的节点的前面，将 cur 移动到第一个要反转的节点的位置上
        pre = dummy
        for i in range(1, left):
             pre = pre.next
        cur = pre.next

        for j in range(0, right - left):
            next_node = cur.next
            cur.next = cur.next.next

            next_node.next = pre.next
            pre.next = next_node

        return dummy.next


if __name__ == "__main__":
    head1 = create_linked_list([1, 2, 3, 4, 5])
    # head2 = create_linked_list([1, 3, 4])
    solution = Solution()
    sorted_lists = solution.reverseBetween(head1,2,4)
    print(print_linked_list(sorted_lists))
#输出：[1, 1, 2, 3, 4, 4]
