def Merge_Two_Sorted_Lists(lst1, lst2):
    i, j = 0,0
    result = []
    while len(lst1)>i and len(lst2)>j:
        if lst1[i]<lst2[j]:
            result.append(lst1[i])
            i+=1
        else:
            result.append(lst2[j])
            j+=1
    result.extend(lst1[i:])
    result.extend(lst2[j:])
    return result
            
            
    
    
    
print(Merge_Two_Sorted_Lists([1, 3, 5],[2, 4, 6]))