def solution(price, money, count):
    answer = 0
    a = price
    for i in range(1, count+1):
        a *= i
        answer += a
        a = price
        print(answer)


    answer = answer - money

    if answer > 0 :
        return answer
    else :
        return 0


