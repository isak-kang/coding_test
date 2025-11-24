def solution(order):
    stack = []

    count = 1
    answer = 0 #답 , 트럭에 실린 수.

    while len(order)+1 >= count:

        if answer >= len(order):
            break
        if stack:
            if stack[-1] == order[answer]:
                answer += 1
                stack.pop(-1)
                continue

        if order[answer] == count :
            answer += 1
        elif  order[answer] != count:
            stack.append(count)



        count += 1

    return answer


order = [5,4,3,2,1]


print(solution([4,3,1,2,5]))