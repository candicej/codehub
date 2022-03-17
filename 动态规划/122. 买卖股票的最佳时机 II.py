# 交易次数不受限，如果可以把所有的上坡全部收集到，一定是利益最大化的
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        sum = cur_sum = 0
        for i in range(1, len(prices)):
            if prices[i] > min:
                cur_sum = prices[i] - min
                sum += cur_sum
            min = prices[i]
        return sum


