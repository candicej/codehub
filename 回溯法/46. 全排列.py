def permute(nums):
    res = []

    def dfs(nums, size, depth, path, used, res):
        # 一个排列中的数字已经选够了
        if depth == size:
            res.append(path[:])
            return

        # 遍历所有可以的元素
        for i in range(size):
            # 判断是否用过
            if not used[i]:
                used[i] = True
                path.append(nums[i])

                # 递归
                dfs(nums, size, depth + 1, path, used, res)

                used[i] = False
                path.pop()

    size = len(nums)
    if not nums:
        return []

    used = [False for _ in range(size)]
    res = []
    dfs(nums, size, 0, [], used, res)

    return res

s = permute([1,2,3])
print(s)