def find_Max_in_List(lst):
    maxValue = -1
    for i in lst:
        if i>maxValue:
            maxValue = i
    return maxValue

print(find_Max_in_List([3, 5, 1, 8]))