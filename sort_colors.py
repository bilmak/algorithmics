# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

def sort_colors_bubble_sort(nums: list[int]):
    if len(nums) <= 1:
        return nums
    pivot = nums[0]
    left = []
    right = []
    for i in range(1, len(nums)):
        if nums[i] < pivot:
            left.append(nums[i])
        else:
            right.append(nums[i])

    return sort_colors(left)+[pivot]+sort_colors(right)


print(sort_colors([2, 0, 2, 1, 1, 0]))


def sort_colors_selection_sort(nums: list[int]) ->None:
    if len(nums) <= 1:
        return 

    n = len(nums)
    for i in range(n):
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    
