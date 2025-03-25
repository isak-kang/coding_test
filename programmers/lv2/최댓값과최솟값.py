# 최댓값 최솟값 구하기

def solution(s):
    s = list(map(int,s.split()))
    min_s = min(s)
    max_s = max(s)
    answer = f"{min_s} {max_s}" 
    return answer

s = '1 2 -2 -5'

print(solution(s))


