def solution(s):
    answer = -1

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')   

    return answer


s = "baabaa"


for i in range(len(s)):
    if s[i] == s[i+1]:
        s[i]
        s.pop(i+1)
            

