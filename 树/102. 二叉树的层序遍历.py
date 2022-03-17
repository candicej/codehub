# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        # 使用队列
        que = [root]
        while que:
            size = len(que)
            # 临时列表，存储了某一层的要么一个要么两个节点
            tmp = []

            # 根据根节点的左右孩子树决定遍历一次还是零次
            for _ in range(size):
                # 根节点
                node = que.pop(0)
                tmp.append(node.val)
                # 把左右孩子加进队列
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            # 这一层的结果遍历结束，把临时列表加进答案里
            res.append(tmp)
        return res
