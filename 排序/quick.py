# 快速排序基于选择划分，是简单选择排序的优化。
# 每次划分将数据选到基准值两边，循环对两边的数据进行划分，类似于二分法。
# 算法的整体性能取决于划分的平均程度，即基准值的选择，此处衍生出快速排序的许多优化方案，甚至可以划分为多块。
# 基准值若能把数据分为平均的两块，划分次数O(logn)，每次划分遍历比较一遍O(n)，时间复杂度O(nlogn)。
# 额外空间开销出在暂存基准值，O(logn)次划分需要O(logn)个，空间复杂度O(logn)


def sortArray(nums):
    def quicksort(nums, left, right):
        flag = nums[(left + right) // 2]  # 每次从中间初始化哨兵位置
        i, j = left, right  # 设定从左到右的指针i，从右到左的指针j
        while i <= j:
            # 注意！！！！ 这里 是找到d小于等于或者大于等于，就是说，不会有遍历完还不交换的情况
            while nums[i] < flag: i += 1  # i从左往右扫，找到大于等于flag的数。
            while nums[j] > flag: j -= 1  # j从右往左扫，找到小于等于flag的数。
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]  # 交换左右指针下标对应的数值
                i += 1  # 左指针继续往右走
                j -= 1  # 右指针继续往左走
        if i < right: quicksort(nums, i, right)  # 递归解决flag左边的低位数组的排序
        if j > left:  quicksort(nums, left, j)  # 递归解决flag右边的低位数组的排序
    quicksort(nums, 0, len(nums) - 1)  # 函数入口，将整个数组的信息传入
    return nums  # 返回修改后的nums

list = [5, 7, 3, 9, 8, 4]
res = sortArray(list)
print(res)