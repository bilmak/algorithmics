def remove_Duplicates_from_List(lst):
    result = []
    for i in lst:
        if i in result:
            continue
        else:
            result.append(i)
    return result
    
    
print(remove_Duplicates_from_List([1, 2, 2, 3]))