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


# 给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。

# 每个元素 nums[i] 表示从索引 i 向后跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:

# 0 <= j <= nums[i] 
# i + j < n
# 返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]
# 
    def least_jump_num(self, nums: List[int]) -> int:
        from queue import Queue
        has_run = [0 for i in range(len(nums))]
        q = Queue(maxsize=len(nums)-1) 
        q.put((0, 0))

        if len(nums) == 1:
            return 0
        while q.qsize() > 0:
            flag = False
            current_src, current_dist = q.get()
     
            for i in range(1, nums[current_src]+1):
                neighbor = i+ current_src

                if neighbor >= len(nums):
                    break
                if not has_run[neighbor]:
                    q.put((neighbor, current_dist + 1))
                    has_run[neighbor] = 1
                if neighbor == len(nums) -1:
                    return current_dist + 1
        return -1
    
    # greedy algorithm
    def least_gpt_jump_num(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return 0
        
        jumps = 0
        current_end = 0  # The farthest we can reach with current number of jumps
        farthest = 0  # The farthest we can reach with the next jump
        
        for i in range(n):
            farthest = max(farthest, i + nums[i])
            
            # If we reach the end of the current jump range
            if i == current_end:
                jumps += 1
                current_end = farthest
                
                # If we can reach the last index, return the result
                if current_end >= n - 1:
                    return jumps
        
        return -1  # If no solution is found
            
def test_jump_num():
    solution = Solution()
    assert solution.least_gpt_jump_num([2, 3, 1, 1, 4]) == 2
    assert solution.least_gpt_jump_num([2, 3, 0, 1, 4]) == 2
    assert solution.least_gpt_jump_num([1, 2, 1, 1, 1]) == 3
    assert solution.least_gpt_jump_num([2, 1, 1, 1, 1]) == 3
    assert solution.least_gpt_jump_num([1, 1, 1, 1, 1]) == 4
    assert solution.least_gpt_jump_num([2, 5, 0, 0]) == 2
    assert solution.least_gpt_jump_num([1, 2, 3]) == 2
    assert solution.least_gpt_jump_num([0]) == 0
    assert solution.least_gpt_jump_num([1]) == 0
    assert solution.least_gpt_jump_num([7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]) == 2

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
                        
                        

                    