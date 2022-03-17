# 冒泡过程可以参考 https://www.bilibili.com/video/BV1Hg4y1q7tz?from=search&seid=2863043788985273873&spm_id_from=333.337.0.0
def bubblesort(arr):
    # 数组长度
    n = len(arr)
    # 因为要遍历 n-1次
    for i in range(1, n):
        # 每次比较两个数，每次最后一个就是最大的，这样最后几个数就是排好序的了
        # n-i就不需要反复对已经排好序的数组排序了
        # 第一个和第二个比较 ，第二个和第三个比较，第三个和第四个比较，把最大冒出去
        for j in range(0, n-i):
            if arr[j] > arr[j+1]:
                # 交换
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

list = [1, 5, 8, 123, 22, 54, 7, 99, 300, 222]
res = bubblesort(list)
print(res)

# 每轮操作O(n)次，共O（n）轮，时间复杂度O(n^2)。
#
# 额外空间开销出在交换数据时那一个过渡空间，空间复杂度O(1)。