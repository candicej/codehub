class Solution:
    def isValidBST(self, root: TreeNode) :
        res = []
        def inorder(root:TreeNode):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)

        for i in range(1,len(res)):
            if res[i] <= res[i-1]:
                return False
        return True