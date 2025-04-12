# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def twoSum(nums: list[int], target: int) -> list[int]:
    for i, k in enumerate(nums):
        for j in range(i+1, len(nums)):
            if k + nums[j]==target:
                return [i, j]
    return []



#twoSum([3,2,4], 6)

def twoSum_second(nums:list[int], target:int)->list[int]:
    output:list=[]
    n = len(nums)
    for i in range(n):
        for j in range(n):
            if nums[i]+nums[j]==target:
                output.append(i)
                output.append(j)
                return output
    return []
