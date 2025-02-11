import pytest
from typing import List

'''
给你一个 非严格递增排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。

考虑 nums 的唯一元素的数量为 k ，你需要做以下事情确保你的题解可以被通过：

更改数组 nums ，使 nums 的前 k 个元素包含唯一元素，并按照它们最初在 nums 中出现的顺序排列。nums 的其余元素与 nums 的大小不重要。
返回 k 。
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        k = 0
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                nums[k] = nums[i]
                k += 1
        nums[k] = nums[len(nums) - 1]
        k += 1

        return k

def test_removeDuplicates():
    solution = Solution()
    
    nums1 = [1, 1, 2]
    k1 = solution.removeDuplicates(nums1)
    assert k1 == 2
    assert nums1[:k1] == [1, 2]
    
    nums2 = [0,0,1,1,1,2,2,3,3,4]
    k2 = solution.removeDuplicates(nums2)
    assert k2 == 5
    assert nums2[:k2] == [0, 1, 2, 3, 4]
    
    nums3 = []
    k3 = solution.removeDuplicates(nums3)
    assert k3 == 0
    assert nums3 == []
    
    nums4 = [1, 2, 3, 4, 5]
    k4 = solution.removeDuplicates(nums4)
    assert k4 == 5
    assert nums4[:k4] == [1, 2, 3, 4, 5]
    
    nums5 = [1, 1, 1, 1, 1]
    k5 = solution.removeDuplicates(nums5)
    assert k5 == 1
    assert nums5[:k5] == [1]

if __name__ == "__main__":
    pytest.main()