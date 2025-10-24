def solution(x, n):
    answer = []
        
    count = 0
    while count < n: # 1 5
        count += 1
        a = x*count # 2 1
        answer.append(a)
        
    return answer