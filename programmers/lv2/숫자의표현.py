def solution(n):
    a,b = 0,1
    for i in range(1,(int(n/2))):
        while a < 15 : # a가 15이상일 떄 종료
            a += i
            i += 1
        if a == 15:
            b +=1
        a = 0
        print(b)
    return b

solution(15)



