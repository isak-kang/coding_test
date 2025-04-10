def solution(n):
    ans = 0
    a = 0    
    
    while n > 0 :
        a += n % 2
        n = n // 2
        
    return a