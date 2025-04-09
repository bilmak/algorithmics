#Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
#Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
#Output: [4,9]
#Explanation: [9,4] is also accepted.

def intersection_array(nums1:list, nums2:list)->list:
    list_intersection:list = []
    if len(nums1)<len(nums2):
        for k in nums1:
            if k in nums2:
                list_intersection.append(k)
            nums2.remove(k)
    else:
        for v in nums2:
            if v in nums1:
                list_intersection.append(v)
            nums1.remove(v)
                
        
    print(list_intersection)
    return list_intersection


intersection_array([1,2,2,1],[2,2])