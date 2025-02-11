import pytest
from typing import List
'''
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素。元素的顺序可能发生改变。然后返回 nums 中与 val 不同的元素的数量。

假设 nums 中不等于 val 的元素数量为 k，要通过此题，您需要执行以下操作：

更改 nums 数组，使 nums 的前 k 个元素包含不等于 val 的元素。nums 的其余元素和 nums 的大小并不重要。
返回 k。
'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p1, p2 = 0, len(nums)-1
        while p1 <= p2:
            if nums[p1] != val:
                p1 += 1
            elif nums[p2] == val:
                p2 -= 1
            else:
                nums[p1] = nums[p2]
                p1 += 1
                p2 -= 1
        return (p2+1)

def test_remove_element():
    solution = Solution()
    
    nums = [3, 2, 2, 3]
    val = 3
    k = solution.removeElement(nums, val)
    assert k == 2
    assert sorted(nums[:k]) == [2, 2]
    
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    k = solution.removeElement(nums, val)
    assert k == 5
    assert sorted(nums[:k]) == [0, 0, 1, 3, 4]
    
    nums = [1]
    val = 1
    k = solution.removeElement(nums, val)
    assert k == 0
    
    nums = [4, 5]
    val = 4
    k = solution.removeElement(nums, val)
    assert k == 1
    assert nums[:k] == [5]
    
    nums = [4, 4, 4, 4]
    val = 4
    k = solution.removeElement(nums, val)
    assert k == 0

if __name__ == "__main__":
    pytest.main()

            
              