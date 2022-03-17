# 从上往下的遍历方法
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root: TreeNode):
            if not root:
                return 0
            return max(height(root.left), height(root.right)) + 1

        if not root:
            return True

        # 首先计算左右子树的高度，如果左右子树的高度差是否不超过 11
        if abs(height(root.left) - height(root.right)) > 1:
            return False

        # 分别递归地遍历左右子节点，并判断左子树和右子树是否平衡
        return self.isBalanced(root.left) and self.isBalanced(root.right)


# 从上往下的遍历方法
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root: TreeNode):
            if not root:
                return 0
            left = height(root.left)
            if left == -1:
                return -1
            right = height(root.right)
            if right == -1:
                return -1
            return max(left, right) + 1 if abs(left - right) < 2 else -1

        return height(root) != -1