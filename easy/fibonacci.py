def fibonacci(n):
    a, b = 0,1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a+b
    return result        
    
    
print(fibonacci(6)) #[0, 1, 1, 2, 3, 5]