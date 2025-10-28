def solution(n):

    answer = []
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    for i in range(1, n//2+1):
        if n % i == 0 :
            if  i not in answer:
                answer.append(i)
                if i != n//i :
                    answer.append(n/i)

    return int(sum(answer))


n=12
print(solution(n))