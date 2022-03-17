# --------------------------------数组----------------------------------------
# 一维数组的定义
import collections

a = [0] * 5
print(a)

# 二维数组
b = [[1] * 2 for i in range(3)]
print(b)
# 地址不同
print(id(b[0]))
print(id(b[1]))

# list.append(obj) 在列表末尾添加新的对象
a.append(3)
print(a)
print(a.count(0))
# 默认最后一个元素
a.pop()

a.insert(3, 2)
print(a)

# ---------------------------队列------------------------------------------------
c = collections.deque()
c.append(4)
c.append(6)
c.popleft()
print(c)
# 如果在 deque 的右边插入，右边弹出，那么就相当于模拟了一个栈。


# -----------------------------哈希表----------------------------------------------
d = {'a': 1, 'b': 3, 'c': 6}
print('字典\n', len(d))
d['d'] = 100
d.pop("c")
# 遍历里面的元素时，是无序的（既不是插入顺序，也不是字典顺序）；


# -----------------------------哈希集合----------------------------------------------
# 空
e = set()
# 非空
e = {3, 4, 6}
e.add(8)
print("哈希集合\n", e)


# ---------------------------链表------------------------------------------------
# 单链表的定义
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


f = ListNode(10)
g = ListNode(9)
f.next = g


# --------------------------二叉树------------------------------------------------
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 构建二叉树
h = TreeNode(20)
i = TreeNode(30)
g = TreeNode(40)
h.left = i
h.right = g

# 插入/删除左孩子或者右孩子的时间复杂度是$O(1)$；
# 适用场景
# 树的变化比较多，考察点丰富，一般会与 BFS、DFS 结合。
# 大部分树题目都是给定了树，让你执行某种操作，很少题目是让你主动选择使用树（特例如字典树）；
# 二叉树相关：深度、翻转、镜像、对称、各种遍历；
# 二叉搜索树相关：验证、搜索、迭代器、范围和；
# 多叉树相关：类似于二叉树。
# 字典树相关：搜索单词、单词替换、单词匹配；