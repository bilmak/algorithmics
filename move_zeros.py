# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

def move(nums:list[int])->list[int]:
    zero_position = 0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[zero_position]=nums[i]
            zero_position+=1
            
    for j in range(zero_position, len(nums)):
        nums[j]=0
        
    return nums


print(move([0,1,0,3,12]))