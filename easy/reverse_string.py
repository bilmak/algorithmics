def reverse(x):
    result = ""
    for i in x:
        result=i+result
    return result

print(reverse("hello"))