# 归并排序的性能不受输入数据的影响，但表现比选择排序好的多，因为始终都是 O(nlogn) 的时间复杂度。代价是需要额外的内存空间
# https://blog.csdn.net/su_bao/article/details/81053871
# 归并排序采用分而治之的原理：
# 一、将一个序列从中间位置分成两个序列；
# 二、在将这两个子序列按照第一步继续二分下去；
# 三、直到所有子序列的长度都为1，也就是不可以再二分截止。这时候再两两合并成一个有序序列即可

def mergesort(seq):
    """归并排序"""
    n = len(seq)
    # 递归结束
    if n <= 1:
        return seq
    # 中间节点
    mid = n // 2  # 将列表分成更小的两个列表
    # 分别对左右两个列表进行处理，分别返回两个排序好的列表
    # 递归 求左半部分
    left = mergesort(seq[:mid])
    # 递归 求右半部分
    right = mergesort(seq[mid:])
    # 对排序好的两个列表合并，产生一个新的排序好的列表
    return merge(left, right)

# 两个数组
def merge(left, right):
    """合并两个已排序好的列表，产生一个新的已排序好的列表"""
    result = []  # 新的已排序好的列表
    i = 0  # 下标
    j = 0
    # 对两个列表中的元素 两两对比。
    # 将最小的元素，放到result中，并对当前列表下标加1
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # 防止有一个列表没有遍历完的情况
    result += left[i:]
    result += right[j:]
    return result

seq = [5,3,0,6,1,4]
result = mergesort(seq)
print(result)

