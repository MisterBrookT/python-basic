'''
给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。
'''
from typing import List
import pytest
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            if nums[i] == 0:
                if i == 0:
                    if len(nums) == 1:
                        return True
                    return False
                elif i == len(nums)-1:
                    return True
                else:
                    check_value = 1
                    j = i-1
                    cannot_jump = True

                    while (j >= 0):
                        if nums[j] > check_value:
                            cannot_jump = False
                            if j+ nums[j] >= len(nums) -1:
                                return True
                        check_value += 1
                        j -= 1           
                        if cannot_jump and j == -1:
                            return False  
        return True
    
    def offcial_implementation(self, nums: List[int]) -> bool:
        max_reach = 0
        for i, num in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + num)
            if max_reach >= len(nums) - 1:
                return True
def test_canJump():
    solution = Solution()
    assert solution.canJump([2, 3, 1, 1, 4]) == True
    assert solution.canJump([3, 2, 1, 0, 4]) == False
    assert solution.canJump([0]) == True
    assert solution.canJump([2, 0, 0]) == True
    assert solution.canJump([1, 1, 1, 1, 1]) == True
    assert solution.canJump([1, 0, 1, 0]) == False
    assert solution.canJump([2, 5, 0, 0]) == True
    assert solution.canJump([1, 2, 3]) == True
    assert solution.canJump([1, 0, 0, 0]) == False

if __name__ == "__main__":
    pytest.main()
                        
                        

                    