#You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

#Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
#Return the maximum number of points you can earn by applying the above operation some number of times.

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        nums.extend([0,0,0])
        prev = [i for i in nums]

        for i in range(len(nums)-4, -1, -1):

            if prev[i] + 1 == prev[i+1]:

                nums[i] = max(nums[i+2] + nums[i], nums[i+3] + nums[i])

            elif prev[i+1] == prev[i]:

                nums[i] = prev[i] + nums[i+1]
                del nums[i+1]

            else:

                nums[i] = max(nums[i+1] + nums[i], nums[i+2] + nums[i])

        return max(nums[0], nums[1])
