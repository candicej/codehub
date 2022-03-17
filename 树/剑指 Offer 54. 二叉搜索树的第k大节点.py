class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        res = []
        def inorder(root:TreeNode):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        # 返回第k个元素
        return res[-k]
