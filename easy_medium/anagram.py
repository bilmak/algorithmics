def anagram_Check(word1, word2):
    word1 = sorted(word1)
    word2 = sorted(word2)
    if word2 == word1:
        return True
    return False

print(anagram_Check("listen", "silent"))
    
    