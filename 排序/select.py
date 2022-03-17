# 选择排序 首先从 未排序的序列中 找到最小的关键码值，接着是从剩余的序列中找到第二小的关键码值
# 独特之处在于交换次序很少
# 无论什么数据进去都是 O(n²) 的时间复杂度。所以用到它的时候，数据规模越小越好。唯一的好处可能就是不占用额外的内存空间了吧
def selectsort(arr):
    n = len(arr)
    # 遍历 n- 1 次 第一次用第一个数和后面的数比较，如果后面的比arr[m]小，就交换
    for i in range(0, n-1):
        # 最小值的索引
        m = i
        # 从比 i 大一个数开始比较
        for j in range(i + 1, n):
            if arr[j] < arr[m]:
                m = j
        if m != i:
            arr[i], arr[m] = arr[m], arr[i]
    return arr

list = [4,1,1,4,2]
res = selectsort(list)
print(res)