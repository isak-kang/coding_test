def solution(absolutes, signs):
    answer = 123456789
    sum_num = 0
    for i in range(len(absolutes)):
        if signs[i] == True:
            sum_num += absolutes[i]
        else :
            sum_num -= absolutes[i]

    return sum_num



