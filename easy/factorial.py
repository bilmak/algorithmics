def factorial(x):
    if x ==0:
        return 1
    return x* factorial(x-1)

print(factorial(5))

def factorials(x):
    result = 1
    for i in range(1, x+1):
        result *=i
    return result

print(factorials(5))