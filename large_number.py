def large(nums:list)->int:
    max = nums[0]
    for i in nums:
        if i>max:
            max=i
    return max


print(large([2,5,8,21,54,6]))