'''
给你一个整数数组 prices ，其中 prices[i] 表示某支股票第 i 天的价格。

在每一天，你可以决定是否购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。你也可以先购买，然后在 同一天 出售。

返回 你能获得的 最大 利润 。
'''
from typing import List
import pytest
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        nums_prices = len(prices)
        buy_price = 10e9
        sell_price = -10e9
        profit = 0
        trade_flag = False
        for i in range(nums_prices):
            if sell_price > 0:
                trade_flag = True
            if not trade_flag:
                if prices[i] <= buy_price:
                    buy_price = prices[i]
                else:
                    sell_price = prices[i]
            else:
                if prices[i] <= sell_price:
                    profit += sell_price - buy_price
                    buy_price = prices[i]
                    sell_price = -10e9
                    trade_flag = False
                else:
                    sell_price = prices[i]
        if sell_price > buy_price:
            profit += sell_price - buy_price
        return profit
    
    def offcial_implement(self, prices):
        profit = 0
        for i in range(len(prices)):
            profit += max(0, prices[i] - prices[i - 1])
        return profit
    
def test_maxProfit():
    solution = Solution()
    assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 7
    assert solution.maxProfit([1, 2, 3, 4, 5]) == 4
    assert solution.maxProfit([7, 6, 4, 3, 1]) == 0
    assert solution.maxProfit([1, 2, 3, 0, 2]) == 4
    assert solution.maxProfit([2, 1, 2, 0, 1]) == 2
    assert solution.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]) == 8
    assert solution.maxProfit([1, 2]) == 1
    assert solution.maxProfit([2, 1]) == 0

if __name__ == "__main__":
    pytest.main()
