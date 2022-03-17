# 有一说一，这道题我不理解，
# 比如 a = [[1,3],[8,10],[2,6],[15,18]]
# 和 排序之后 [[1,3],[2,6]，[8,10],[15,18]] 出来的结果明明不一样啊，怎么可以排序的？

# 更新，回答上面的， 我懂了，这个合并区间是针对全局的，就像上面的例子，
# 按照我之前的想法 答案应该是 [1,3] [8,10] [2,6] [15,18] 这里面显然有很多重复的区间，所以说不是两两合并，可以把这些区间弄在一个坐标轴上，这样就可以理解了。
# 因此是可以排序的


# 官方题解
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 排序
        intervals.sort(key=lambda x: x[0])

        # 答案
        merged = []
        for interval in intervals:
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            # merged[-1] 就是已经合并完的最后一个元素，如果新元素大于merged[-1][1]，就不存在重合
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            # 否则 更新 merged[-1][1]
            else:
                # 否则的话，我们就可以与上一区间进行合并
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


# 这个解法一般
# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         ret = []
#         intervals.sort()
#         start, end = intervals[0]
#         for interval in intervals:
#             # 如果下一个元素的第一个数 比 end 大 说明不存存重合 直接把上一次的start 和 end加进结果
#             if interval[0] > end:
#                 ret.append([start, end])
#                 # start更新一下
#                 start = interval[0]
#             #
#             end = max(end, interval[1])
#         ret.append([start, end])
#         return ret