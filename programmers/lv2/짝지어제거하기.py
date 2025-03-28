# 짝지어지면 삭제
# 스택을 이용해 처리......
# 못풀어서 도움받음.

def solution(s):
    answer = -1

    for i in range(len(s)):
        stack = []
        if not stack:
            stack.append(s[i])
        else:
            if s[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
    if not stack:
        answer = 1
    else :
        answer = 0   

    return answer