# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 方法一 递归法
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def inorder(root: TreeNode):
            # 终止条件：当前节点为空时
            if not root:
                return
            # 递归的调用左节点，打印当前节点，再递归调用右节点
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        # 调用函数
        inorder(root)
        return res


# 方法二 迭代法 使用一个固定的模板
class Solution:
    # 参考 迭代 https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/dong-hua-yan-shi-94-er-cha-shu-de-zhong-xu-bian-li/
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        while stack or root:
            # 不断往左子树方向走，每走一次就将当前节点保存到栈中
            # 这是模拟递归的调用
            if root:
                stack.append(root)
                root = root.left
            # 当前节点为空，说明左边走到头了，从栈中弹出节点并保存
            # 然后转向右边节点，继续上面整个过程
            else:
                # 左子树为空了，弹出栈顶元素。寻找上一个节点的右节点，并加入栈
                tmp = stack.pop()
                res.append(tmp.val)
                root = tmp.right
        return res




