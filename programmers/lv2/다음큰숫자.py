# 다음으로 큰숫자 맞추기 2진수로 했을 때 1의갯수가 같아야함.

def solution(n):
    answer = 0

    a,b = 0,0
    
    a = str(bin(n)[2:]).count("1")

    while b != a :   
        n += 1
        b = str(bin(n)[2:]).count("1")

    answer = n

    return answer

print(solution(2000))


