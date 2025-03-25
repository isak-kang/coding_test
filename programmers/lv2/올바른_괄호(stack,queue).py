# 올바른 괄호

def solution(s):
    stack = []
    answer = False
    for i in s:
        if i == "(":
            stack.append(i)
        else :
            if "(" not in stack :
                return answer
            else :
                stack.pop()
    
    if "(" in stack:
        return answer
    
    answer = True
    return answer


# 처음에 pop(0)으로 해서 시간복잡도 올라가서 효율성에서 떨어짐
# 첫번째요소 삭제마다 한칸씩밀려서 시간복잡도가 O(n)이 됨.
# stack을 큐처럼 사용x 단순 스택으로 사용