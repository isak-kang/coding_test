def test(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    a,b = 1,2
    for i in range(2,n): # 2
        
        a, b = b, a+b
        print(a,b)
    return b

print(test(7))


zxzx