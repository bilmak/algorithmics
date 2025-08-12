def count_Vowels_in_String(text):
    vovels = ["A","E", "I", "O", "U"]
    bigger = text.upper()
    result = 0
    for i in bigger:
        if i in vovels:
            result+=1
    return result
            
print(count_Vowels_in_String("hello world"))