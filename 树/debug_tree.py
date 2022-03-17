# 节点类
class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 树生成代码
def generate_tree(vals):
    if len(vals) == 0:
        return None
    que = [] # 定义队列
    fill_left = True # 由于无法通过是否为 None 来判断该节点的左儿子是否可以填充，用一个记号判断是否需要填充左节点
    for val in vals:
        node = Node(val) if val else None # 非空值返回节点类，否则返回 None
        if len(que)==0:
            root = node # 队列为空的话，用 root 记录根结点，用来返回
            que.append(node)
        elif fill_left:
            que[0].left = node
            fill_left = False # 填充过左儿子后，改变记号状态
            if node: # 非 None 值才进入队列
                que.append(node)
        else:
            que[0].right = node
            if node:
                que.append(node)
            que.pop(0) # 填充完右儿子，弹出节点
            fill_left = True #
    return root


# def inorderTraversal(root):
#     res = []
#
#     def inorder(root):
#         # 终止条件：当前节点为空时
#         if not root:
#             return
#         # 递归的调用左节点，打印当前节点，再递归调用右节点
#         inorder(root.left)
#         res.append(root.val)
#         inorder(root.right)
#     # 调用函数
#     inorder(root)
#     return res

# 参考 迭代 https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/dong-hua-yan-shi-94-er-cha-shu-de-zhong-xu-bian-li/
def inorderTraversal(root):
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



def levelOrder(root):
    if not root:
        return
    res = []
    que = [root]
    while que:
        size = len(que)
        tmp = []

        for _ in range(size):
            node = que.pop(0)
            tmp.append(node.val)
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        res.append(tmp)
    return res


def isValidBST(root):
    res = []
    def inorder(root):
        if not root:
            return
        inorder(root.left)
        res.append(root.val)
        inorder(root.right)
    for i in range(1,len(res)):
        if res[i] < res[i-1]:
            return False
    return True

def isBalanced(root):
    def height(root):
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

# test
null = None
vals = [1,2,2,3,3,null,null,4,4]
tree = generate_tree(vals)
print('中序遍历:')
a = isBalanced(tree)
print(a)

