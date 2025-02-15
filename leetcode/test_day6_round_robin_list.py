'''
给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
'''
from typing import List
import pytest
import math
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        k = k % len_nums  # In case k is greater than the length of nums
        gcd = math.gcd(len_nums, k)
        for i in range(gcd):
            start_value = nums[i]
            start_p = i
            end_p = (start_p + k) % len_nums
            self.recursive_assign(i, k, start_p, end_p, nums)
            nums[end_p] = start_value

    def recursive_assign(self, i, k, start, end, nums, flag=False):
        if start == i:
            if flag:
                return nums
            else:
                flag = True
        next_start = (start + k) % len(nums)
        next_end = (end + k) % len(nums)
        self.recursive_assign(i, k, next_start, next_end, nums, flag)
        nums[end] = nums[start]

    @staticmethod
    def rotate_better_version(nums: List[int], k: int) -> None:
        len_nums = len(nums)
        k = k % len_nums  # In case k is greater than the length of nums
        gcd = math.gcd(len_nums, k)
        for start in range(gcd):
            current = start
            next = (start + k) % len_nums
            temp = nums[current]
            while next != start:
                nums[next], temp = temp, nums[next]
                current = (current + k) % len_nums
                next = (next + k) % len_nums
            nums[next], temp = temp, nums[next]



def test_rotate():
    sol = Solution()
    
    nums = [1, 2, 3, 4, 5, 6, 7]
    sol.rotate(nums, 3)
    assert nums == [5, 6, 7, 1, 2, 3, 4]
    
    nums = [-1, -100, 3, 99]
    sol.rotate(nums, 2)
    assert nums == [3, 99, -1, -100]
    
    nums = [1, 2, 3, 4, 5, 6]
    sol.rotate(nums, 4)
    assert nums == [3, 4, 5, 6, 1, 2]
    
    nums = [1, 2]
    sol.rotate(nums, 3)
    assert nums == [2, 1]
    
    nums = [1]
    sol.rotate(nums, 0)
    assert nums == [1]

if __name__ == "__main__":
    Solution().rotate_better_version(nums=[1, 2, 3, 4, 5, 6, 7], k=1)
    