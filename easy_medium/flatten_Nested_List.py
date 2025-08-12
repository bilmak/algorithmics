def flatten_Nested_List(lst):
    result = []
    for i in lst:
        for j in i:
            result.append(j)
        
    return result    


print(flatten_Nested_List([[1, 2], [3, 4]])) #[1, 2, 3, 4]