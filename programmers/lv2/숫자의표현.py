# 이지 연속된 숫자를 더해서 n값나오는거 갯수 찾기기

def solution(n):
    a,b = 0,0
    for i in range(1,n+1):
        while a < n : # a가 n이상일 떄 종료
            a += i
            i += 1
        if a == n:
            b +=1
        a = 0
        print(b)
    return b