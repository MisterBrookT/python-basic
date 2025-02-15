'''
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
'''
from typing import List
import pytest
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        if days == 0:
            return 0
        profit_list = [[0, 0] for _ in range(days)]
        p1, p2 = 0, days - 1
        for i in range(days):
            if i == 0:
                profit_list[p1][0] = prices[p1]
                profit_list[p2][1] = prices[p2]
            else:
                profit_list[p1][0] = min(profit_list[p1 - 1][0], prices[p1])
                profit_list[p2][1] = max(profit_list[p2 + 1][1], prices[p2])
            p1 += 1
            p2 -= 1
        return max([t[1] - t[0] for t in profit_list])

    def official_solution(self, prices: List[int]) -> int:
        inf = int(1e9)
        minprice = inf
        maxprofit = 0
        for price in prices:
            maxprofit = max(price - minprice, maxprofit)
            minprice = min(price, minprice)
        return maxprofit

def test_maxProfit():
    solution = Solution()
    assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert solution.maxProfit([7, 6, 4, 3, 1]) == 0
    assert solution.maxProfit([1, 2, 3, 4, 5]) == 4
    assert solution.maxProfit([5, 4, 3, 2, 1]) == 0
    assert solution.maxProfit([2, 4, 1]) == 2
    assert solution.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]) == 4
    assert solution.maxProfit([]) == 0
    assert solution.maxProfit([1]) == 0

if __name__ == "__main__":
    pytest.main()

        