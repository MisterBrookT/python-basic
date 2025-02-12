from typing import List
import pytest
'''
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = 0
        while (p1+2) <= (len(nums) -1): 
            if nums[p1] == nums[p1+2]:
                nums.pop(p1+2)
            else:
                p1 += 1
        return len(nums)

def test_removeDuplicates():
    solution = Solution()
    
    nums1 = [1, 1, 1, 2, 2, 3]
    assert solution.removeDuplicates(nums1) == 5
    assert nums1 == [1, 1, 2, 2, 3]
    
    nums2 = [0,0,1,1,1,1,2,3,3]
    assert solution.removeDuplicates(nums2) == 7
    assert nums2 == [0, 0, 1, 1, 2, 3, 3]
    
    nums3 = [1, 1, 1, 1, 1, 1]
    assert solution.removeDuplicates(nums3) == 2
    assert nums3 == [1, 1]
    
    nums4 = [1, 2, 3, 4, 5]
    assert solution.removeDuplicates(nums4) == 5
    assert nums4 == [1, 2, 3, 4, 5]
    
    nums5 = []
    assert solution.removeDuplicates(nums5) == 0
    assert nums5 == []

if __name__ == "__main__":
    pytest.main()
    