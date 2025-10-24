def solution(n):
    answer = 0
    # n % s = 1
    for i in range(2,n):
        if n % i == 1:
            return i
