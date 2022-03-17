# 执行过程可以参考https://leetcode-cn.com/problems/diameter-of-binary-tree/solution/shi-pin-jie-shi-di-gui-dai-ma-de-yun-xing-guo-chen/
# 也就是找出来那个节点的左右子树高度的和最大
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 1
        def height(root):
            if not root:
                return 0
            # 先求左子树的高度
            left = height(root.left)
            # 再求右子树的高度
            right = height(root.right)
            # 答案
            self.ans = max(left + right + 1, self.ans)
            # 高度是左右子树大的那个
            return max(left,right) + 1
        height(root)
        return ans -1