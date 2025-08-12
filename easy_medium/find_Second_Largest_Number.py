def find_Second_Largest_Number(lst):
    result = sorted(lst)
    return result[-2]
    
    
print(find_Second_Largest_Number([10, 20, 4, 45, 99])) #45