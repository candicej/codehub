# 数组的前面部分是有序序列，每次找到有序序列后面的第一个元素（待插入元素）的插入位置，
# 将有序序列中的插入位置后面的元素都往后移动一位，然后将待插入元素置于插入位置。

def insertsort(nums):
    n = len(nums)
    for i in range(1, n):
        # 前面i个数字是排好序的
        j = i
        # 用k把当前需要排序的数字存储起来
        key = nums[i]
        # j这里大于0 是因为 要和前面的一个进行比较，所以必须大于0
        while key < nums[j-1] and j > 0:
            # 如果比前面的小，说明需要把大的那个换一下
            nums[j] = nums[j-1]
            # 再和前一个的前一个比较
            j -= 1
            # 最后 赋值
        nums[j] = key
    return nums

list = [5, 1, 8, 54, 7, 99, 30, 80]
res = insertsort(list)
print(res)
