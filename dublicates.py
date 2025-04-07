#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Explanation:
# The element 1 occurs at the indices 0 and 3.

def find_dublicates(nums:list)->bool:
    nums_dict:dict = {}
    count = 1
    for k in nums:
        if k in nums_dict:
            count+=1
            return False
        nums_dict[k]= count
    print(nums_dict)
    return True

find_dublicates([3,4,2, 3])