# 参考 https://www.bilibili.com/video/BV1fp4y1D7cj/?spm_id_from=333.788.recommend_more_video.0
# https://shazhenyu.blog.csdn.net/article/details/91395700
# https://blog.csdn.net/june_young_fan/article/details/82014081

# 排序的思路是 ：首先将待排序序列构造成一个大顶堆，
# 此时，整个序列的最大值就是堆顶的根节点。将其与末尾元素进行交换，此时末尾就为最大值。
# 可称为有序区，然后将剩余n-1个元素重新构造成一个堆，估且称为堆区(未排序)。这样会得到n个元素的次小值。
# 重复执行，有序区从:1--->n，堆区：n-->0，便能得到一个有序序列了

# 建立最大堆
def buildMaxHeap(arr):
    # 堆的大小
    size = len(arr)
    # 从 n/2 向下取整的节点开始 进行heapify （规则
    for i in range(size//2, -1, -1):
        heapify(arr, size, i)


# 大根堆调整（max_heapify）
# 将堆的末端子节点作调整，使得子节点永远小于父节点
# 从一个节点出发，
def heapify(arr, size, i):
    left = 2*i+1
    right = 2*i+2
    largest = i
    if left < size and arr[left] > arr[largest]:
        largest = left
    if right < size and arr[right] > arr[largest]:
        largest = right
    # 如果最大节点不是 父节点，交换
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # 对以旧的largest 为节点做heapfiy，防止调整后的largest节点比她的孩子节点小
        heapify(arr, size, largest)

# 堆排序
def heapSort(arr):
    # 建立最大堆
    buildMaxHeap(arr)
    # 调整后列表的第一个元素就是这个列表中最大的元素，将其与最后一个元素交换，然后将剩余的列表再递归的调整为最大堆
    # 为什么i 不断减小，因为后面是已经排好序的数组了，不需要建堆了
    for i in range(len(arr)-1, -1, -1):
        # arr[0] 是最大的，将其和最后一个元素交换，使得最后一个元素的值最大，
        arr[0], arr[i] = arr[i], arr[0]
        # 堆 的大小，随着遍历不断减小
        heapify(arr, i, 0)
    return arr

if __name__ == '__main__':
    list = [31, 5, 8, 123, 22, 54, 7]
    print("List source is:", list)
    result = heapSort(list)
    print("List sort is:", result)


