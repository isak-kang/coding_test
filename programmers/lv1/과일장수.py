def solution(k, m, score):
    score.sort(reverse = True)

    answer = score[m] * m
        
    return answer

k=4
m=3
score = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]
score.sort(reverse = True)

answer = score[m] * m

print(answer,score[m],score)

print(solution(k, m, score))