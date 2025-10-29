def solution(n):
    answer = ""
    n = str(n)
    a = []
    for i in n:
        a.append(i)
    a.sort(reverse=True)
    for i in a :

        answer += i

    return int(answer)


n = 123132555
print(solution(n))