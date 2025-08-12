def longest_Word_in_a_Sentence(text):
    words = text.split()
    result = ""
    for i in words:
        if len(i)>len(result):
            result = i
    
    return result
        
    
    
    
print(longest_Word_in_a_Sentence("Python is great"))