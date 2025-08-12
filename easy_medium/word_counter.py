def word_Frequency_Counter(text):
    result = {}
    words = text.split()
    for i in words:
        if i not in result:
            result[i]=1
        else:
            result[i]+=1
    return result

print(word_Frequency_Counter("apple banana apple"))