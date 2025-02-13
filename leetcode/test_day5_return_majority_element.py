'''
给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。
'''
from typing import List, Tuple
import pytest
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1  
        max_element, max_num = 0, 0
        for element, num in count.items():
            if max_num < num:
                max_element = element
                max_num = num
        return max_element

def test_majority_element():
    solution = Solution()
    assert solution.majorityElement([3, 2, 3]) == 3
    assert solution.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
    assert solution.majorityElement([1]) == 1
    assert solution.majorityElement([1, 1, 1, 2, 2]) == 1
    assert solution.majorityElement([4, 4, 4, 4, 4, 5, 5, 5, 5]) == 4

if __name__ == "__main__":
    pytest.main()