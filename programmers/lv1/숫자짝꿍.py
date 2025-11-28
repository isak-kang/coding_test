def solution(X, Y):
    answer = ''

    X_conut = [0] * 10
    Y_conut = [0] * 10
    for ch in X :
        X_conut[int(ch)] += 1
    for ch in Y:
        Y_conut[int(ch)] += 1


    for i in range(9,-1,-1):
        min_num = min(X_conut[i],Y_conut[i])
        answer += str(i)*min_num

    if answer == "":
        return "-1"
    if answer[0] == "0":
        return "0"

    return str(answer)

