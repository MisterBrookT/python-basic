from typing import List
import pytest
'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
'''
class Solution:
    @staticmethod
    def my_solution(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i  = m + n - 1
        m -= 1
        n -= 1
        # merged sort
        if m < 0:
            nums1[:n+1] = nums2[:n+1]
        while m>=0 and n>=0:
            if nums1[m] > nums2[n]:
                nums1[i] = nums1[m]
                m -= 1
                i -= 1
                if m < 0:
                    nums1[:n+1] = nums2[:n+1]
            else:
                nums1[i] = nums2[n]
                i -= 1
                n -= 1

    @staticmethod
    def official_solution(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m - 1, n - 1
        tail = m + n - 1
        while p1 >= 0 or p2 >= 0:
            if p1 == -1:
                nums1[tail] = nums2[p2]
                p2 -= 1
            elif p2 == -1:
                nums1[tail] = nums1[p1]
                p1 -= 1
            elif nums1[p1] > nums2[p2]:
                nums1[tail] = nums1[p1]
                p1 -= 1
            else:
                nums1[tail] = nums2[p2]
                p2 -= 1
            tail -= 1

import pytest

def test_mysolution():
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    m = 3
    n = 3
    Solution.my_solution(nums1, m, nums2, n)
    assert nums1 == [1, 2, 2, 3, 5, 6]

def test_merge_with_empty_mysolution():
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = []
    m = 3
    n = 0
    Solution.my_solution(nums1, m, nums2, n)
    assert nums1 == [1, 2, 3, 0, 0, 0]

def test_merge_with_empty_mysolution():
    nums1 = [0, 0, 0]
    nums2 = [2, 5, 6]
    m = 0
    n = 3
    Solution.my_solution(nums1, m, nums2, n)
    assert nums1 == [2, 5, 6]

def test_merge_with_all_mysolution():
    nums1 = [0, 0, 0]
    nums2 = [0, 0, 0]
    m = 0
    n = 3
    Solution.my_solution(nums1, m, nums2, n)
    assert nums1 == [0, 0, 0]

if __name__ == "__main__":
    pytest.main()
