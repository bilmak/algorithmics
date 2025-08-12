def check_palidrome(text):
    ln = len(text)
    for i in range(ln//2):
        if text[i]!=text[ln-i-1]:
            return False
        return True
    
print(check_palidrome("madam"))
    