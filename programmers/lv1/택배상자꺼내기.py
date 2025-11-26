def solution(n, w, num):
    answer = 0
    amount_list = []
    line_list = [0] * w

    for i in range(1, n+1):
        line_list[((i-1) % w)] = i

        if i % w == 0 or i == n:
            amount_list.append(line_list)
            line_list = [0] * w

    for j in range(len(amount_list)):
        if j % 2 == 1:
            amount_list[j] = list(reversed(amount_list[j]))



    for k in range(len(amount_list)):
        try :
            second_index_num = amount_list[k].index(num)
            first_index_num = k
            break
        except:
            pass

    if k == len(amount_list)-1:
        answer = 0

    elif amount_list[-1][second_index_num] == 0:
        answer = len(amount_list) - 1  -k
    else :
        answer = len(amount_list)  - k

    return answer



answer =0
n = 22
w =6
num = 8



print(answer)
