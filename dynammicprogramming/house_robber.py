#You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

#Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

class Solution:
    def rob(self, nums: List[int]) -> int:
    
        nums.extend([0,0,0])

        for j in range(len(nums)-4, -1, -1):
            
            nums[j] = max(nums[j+2] + nums[j], nums[j+3] + nums[j]) 
            
        return max(nums[0], nums[1])
