from binascii import a2b_base64


def solution(s):
    answer = []
    memo_s = []
    for i in s:
        if i in memo_s:
            a = len(memo_s) - 1 - memo_s[::-1].index(i)
            answer.append(len(memo_s)-a)
        else :
            answer.append(-1)
        memo_s.append(i)

    return answer

#
s = "banana"
print(solution(s))