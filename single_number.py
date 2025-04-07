# #Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.
# Example 1:
# Input: nums = [2,2,1]
# Output: 1

def single(nums: list) -> int:
    single_numbers: dict = {}

    for k in nums:
        count = 1
        if k in single_numbers:
            count += 1
        single_numbers[k] = count

    for k in single_numbers:
        if single_numbers[k] == 1:
            return k
    return -1


single([1])
