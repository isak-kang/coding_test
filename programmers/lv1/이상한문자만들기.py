

def solution(s):
    answer = ''
    for i in range(len(s)):
        if s[i] == " ":
            answer += s[i]
        else :
            if i % 2 == 0:
                answer += s[i].upper()
            else :
                answer += s[i].lower()

    return answer
s = "asd asd"
print(solution(s))